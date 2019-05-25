from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(default='default.jpg',upload_to = 'projectImages')
    description = models.TextField()
    
    
    def __str__(self):
        return f'{self.title}'