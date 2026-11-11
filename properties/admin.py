from django.contrib import admin
from django.utils import timezone
from .models import Property, PropertyImage


# Register your models here.
class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 0

@admin.action(description="Approve selected listings")
def approve_listings(modeladmin, request, queryset):
    queryset.update(
        status = Property.Status.APPROVED,
        reviewed_at = timezone.now(),
    )

@admin.action(description="Reject selected listings")
def reject_listings(modeladmin, request, queryset):
    queryset.update(
        status=Property.Status.REJECTED,
        reviewed_at=timezone.now(),
    )

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display= (
        "title", "landlord", "area", "monthly_rent", "status", "submitted_at",
    )
    list_filter = ("status", "property_type", "area")
    search_fields = ("title", "area", "landmark", "landlord_username")
    readonly_fields = ("created_at", "updated_at", "submitted_at")
    inlines = [PropertyImageInline]
    actions = [approve_listings, reject_listings]

    fieldsets = (
        ("Listing details",{
            "fields":(
                "landlord", "title", "description", "area", "landmark", "property_type", "monthly_rent", "deposit", "bedrooms", "available_from",
            )
        }),
        ("Moderation",{
            "fields":("status", "admin_note", "reviewed_at")
        }),
        ("Timestamps",{
            "fields":("submitted_at", "created_at", "updated_at")
        }),
    )
@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ("property", "uploaded_at")