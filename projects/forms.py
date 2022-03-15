from django import forms
from .models import Project
from .models import *

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('description', 'title', 'technology', 'image')
    