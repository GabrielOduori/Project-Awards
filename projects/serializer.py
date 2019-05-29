from accounts.models import Profile
from projects.models import Project

from rest_framework import serializers



class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = (
            'user',
            'bio',
            'email'
        )
        
        
class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = (
            'title',
            'description', 
            'profile', 
            'pub_date',
            'website'
        )