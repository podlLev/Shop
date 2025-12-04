from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField

from accounts.models import Profile


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email address",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email',
            'class': 'form-control'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Username',
            'password1': 'Password',
            'password2': 'Confirm password',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Choose a username',
            'class': 'form-control'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Enter a secure password',
            'class': 'form-control'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Repeat your password',
            'class': 'form-control'
        })

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered.")
        return email


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        label="Email address",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email',
            'class': 'form-control'
        })
    )

    first_name = forms.CharField(
        required=False,
        label="First name",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your first name',
            'class': 'form-control'
        })
    )

    last_name = forms.CharField(
        required=False,
        label="Last name",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your last name',
            'class': 'form-control'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Enter your username',
                'class': 'form-control'
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.exclude(pk=self.instance.pk).filter(email=email)
        if qs.exists():
            raise forms.ValidationError("This email address is already in use.")
        return email


class ProfileUpdateForm(forms.ModelForm):
    phone = PhoneNumberField(
        required=False,
        error_messages={
            'invalid': 'Enter a valid Ukrainian phone number (e.g. +380 67123 45 67).'
        },
        widget=forms.TextInput(attrs={
            'placeholder': '+380XXXXXXXXX',
            'class': 'form-control'
        })
    )

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'location', 'phone', 'birth_date']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'bio': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Tell us about yourself...',
                'class': 'form-control'
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'City, Country',
                'class': 'form-control'
            }),
            'birth_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
        }
