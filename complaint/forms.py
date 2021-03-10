from django import forms
from . import models


class registrationForm(forms.ModelForm):
    class Meta:
        model = models.UserEmail
        fields = '__all__'


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = models.Complaint
        fields = '__all__'

