from django.forms import ModelForm
from .models import Enrollment
from django import forms

class EnrollmentForm(ModelForm):

    class Meta:
        model = Enrollment
        fields = [ 'grade']  
