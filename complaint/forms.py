from django import forms
from . import models


class registrationForm(forms.ModelForm):
    class Meta:
        model = models.UserEmail
        # include all fields of the class
        fields = '__all__'


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = models.Complaint
        # include all fields of the class
        fields = '__all__'

