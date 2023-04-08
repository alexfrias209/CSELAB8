from django.forms import ModelForm, ValidationError
from .models import Enrollment
from django import forms

class EnrollmentForm(ModelForm):
    grade = forms.DecimalField(localize=True, required=False)
    id = forms.ModelChoiceField(queryset=Enrollment.objects.all(), widget=forms.HiddenInput())  # Add this line

    class Meta:
        model = Enrollment
        fields = ['id', 'grade']  # Add 'id' to fields
