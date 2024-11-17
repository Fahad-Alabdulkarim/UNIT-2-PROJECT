from django import forms
from .models import Project,Images

class ProjectForm(forms.ModelForm):
    
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
    

    
    class Meta:
        model = Project
        fields = ['name', 'description', 'tools', 'date', 'github_link']

    

class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['images']