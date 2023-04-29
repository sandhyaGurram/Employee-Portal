from django import forms
from django.forms import ModelForm
from . models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['fname', 'email', 'phone', 'experiance', 'skills', 'role', 'location']
