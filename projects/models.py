from django.db import models
from django.core.validators import URLValidator
from accounts.models import Profile

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'projects/')
    website = models.TextField(validators=[URLValidator()])
    
    class Meta:
        ordering = ["pub_date"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return f'{self.title}'
    
    
    def summary(self):
        return self.description[:100]+" ......"
    
    
    def save_project(self):
        self.save()
        
    def delete_project(self):
        self.delete()
        
    @classmethod
    def search_project(cls, term):
        searched_images = cls.objects.filter(project__titile__icontains = term)
        return searched_images
    
    @classmethod
    def get_projects(cls):
        projects = Project.objects.all()
        
        return projects
    
    
class Review(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    author  =  models.ForeignKey(Profile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    
    
    def __str__(self):
        return f'{self.body}'
    
     
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        
        
    def save_review(self):
        self.save()
        
        
    def delete_review(self):
        self.delete()