from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import SignUpForm


# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Your account has been created.")
            return redirect("dashboard")
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form})   
