from django import forms
from accounts.models import User


class UserRegistration(forms.ModelForm):
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'e.g. 9769798529'}
        ),
        required=True,
        label='Phone Number'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        ),
        required=True,
        label='Password'
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        ),
        required=True,
        label='Confirm Password'
    )

    class Meta:
        model = User
        fields = ['phone_number', 'password']

    def clean(self):
        clean_data = super().clean()
        if not clean_data.get('phone_number', False):
            raise forms.ValidationError(
                'This field is required.', code='invalid')
        elif len(clean_data['phone_number']) != 10:
            raise forms.ValidationError(
                'Phone number should be excatly 10 digits', code='invalid')

        if not clean_data.get('password', False):
            raise forms.ValidationError(
                'Password field is required.', code='invalid')
        elif len(clean_data['password']) != 8:
            raise forms.ValidationError(
                'This password is too short. It must contain at least 8 characters.',
                code='invalid'
            )

        if clean_data['password'] != clean_data.get('confirm_password', False):
            raise forms.ValidationError('Passwords don\'t match')
        return clean_data

    def save(self, commit=True):
        clean_data = super().clean()
        user = super(UserRegistration, self).save(commit=False)
        user.set_password(clean_data['password'])
        if commit:
            user.save()
        return user


class UserLogin(forms.Form):
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'e.g. 9769798529'}
        ),
        required=True,
        label='Phone Number'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        ),
        required=True,
        label='Password'
    )

    def clean(self):
        clean_data = super().clean()
        return clean_data
