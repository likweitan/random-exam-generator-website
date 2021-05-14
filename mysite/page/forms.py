from django import forms
from .models import Attempt

class SubmitForm(forms.Form):
    student_id = forms.CharField(max_length=10,label = "学号")