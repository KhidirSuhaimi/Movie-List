from movieForms.models import Project
from django import forms

class ProjectForms(forms.ModelForm):
    class Meta: 
        model = Project
        fields = '__all__'