from django import forms
from projects.models import Project, Review

class AddProjectForm(forms.ModelForm):
    class Meta:
        
        model = Project
        fields = (
            'title',
            'image',
            'description',
            'website'
            )
    
    

class ReviewForm(forms.Form):
    class Meta:
        model = Review
        fields = (
            'body',
        )