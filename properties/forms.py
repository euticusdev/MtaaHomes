from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            "title",
            "description",
            "area",
            "landmark",
            "property_type",
            "monthly_rent",
            "deposit",
            "bedrooms",
            "available_from",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 5}),
            "available_from": forms.DateInput(attrs={"type": "date"}),
        }
        def clean_monthly_rent(self):
            value = self.cleaned_data["monthly_rent"]
            if value<= 0:
                raise forms.ValidationError("Rent must be greater than zero")
            return value 