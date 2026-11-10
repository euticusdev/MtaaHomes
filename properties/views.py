from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


from accounts.models import User
from .forms import PropertyForm
from .models import Property, PropertyImage


def home(request):
    listings = Property.objects.filter(
        status = Property.Status.APPROVED

    ) .prefetch_related("images") [:12]
    return render(request, "properties/home.html", {"listings": listings})

@login_required
def dashboard(request):
    if request.user.role == User.Role.LANDLORD:
        listings = Property.objects.filter(landlord=request.user)
    else:
        listings = Property.objects.filter(
            status = Property.Status.APPROVED
        )
    return render(
        request,
        "properties/dashboard.html",
        {"listings": listings},
    )
@login_required
def create_property(request):
    if request.user.role != User.Role.LANDLORD:
        raise PermissionDenied("Only landlords can submit properties.")
    if request.method == "POST":
        form = PropertyForm(request.POST)
        images = request.FILES.getlist("images")
        if form.is_valid():
            if len(images) > 8:
                form.add_error(None, "Upload a maximum of 8 photos.")
            else:
                prop = form.save(commit=False)
                prop.landlord = request.user
                prop.status = Property.Status.PENDING
                prop.save()

                for image in images:
                    PropertyImage.objects.create(
                        property = prop,
                        image = image,
                    )

                messages.success(
                    request,
                    "Listing submitted. It is pending for admin to review.",
                )
                return redirect("dashboard")
        else:
            form = PropertyForm()
        return render(
            request,
            "properties/property_form.html",
            {"form": form},
        )
    def property_detail(request, pk):
        prop = get_object_or_404(
            Property.objects.prefetch_related("images"),
            pk=pk,
            status = Property.Status.APPROVED,
        )
        return render(
            request,
            "properties/property_detail.html",
            {"property": prop},
        )