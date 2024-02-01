from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField(
        validators=[
            EmailValidator(message='Enter a valid email address.'),
        ]
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data["email"]
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists!")
        return email

    def validate_unique_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise ValidationError("A user with this email already exists!")

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        if email:
            self.validate_unique_email(email)