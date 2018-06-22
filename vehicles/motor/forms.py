from django import forms
from motor.models import Motor
import re


class MotorForm(forms.ModelForm):
    vehical_number = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'e.g. MH03CB8906'}),
        required=True,
        max_length=45
    )
    policy = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=Motor.POLICY,
        required=True
    )


    class Meta:
        model = Motor
        fields = ['vehical_number', 'policy']
        labels = {
            'vehical_number': 'Vehical Number',
            'policy': 'Do you have a Policy'
        }

    def clean_vehical_number(self):
        vnum = super().clean()
        match = re.match('^(MH){1}[0-9]{2}[A-Z]{2}[0-9]{4}', vnum['vehical_number'])
        if not match:
            raise forms.ValidationError('Vehical Number Incorrect', code='invalid')
        else:
            return vnum
