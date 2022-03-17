from django import forms
from .models import *

class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, member):
        return "%s" % member.name

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('description', 'title', 'technologies', 'image')
    technologies = CustomMMCF(
        queryset=Technology.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    