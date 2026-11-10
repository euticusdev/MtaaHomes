from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields =(
            "username",
            "email",
            "phone_number",
            "role",
            "password1",
            "password2",
        )
    def clean_role(self):
        role = self.cleaned_data["role"]
        if role not in (User.Role.SEEKER, User.Role.LANDLORD):
            raise forms.ValidationError("Choose a valid account type.")
        return role