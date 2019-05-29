from django.test import TestCase
from .models import Project, Review
from accounts.models import Profile
from django.contrib.auth.models import User

# Create your tests here.


class ProjectTestClass(TestCase):
    
    def setUp(self):
        self.user1 = User(
            username = 'test1',
            password =  'tehsingpass'
            )
        
        self.profile1 = Profile (
 
             user = self.user1,
             bio = 'This is great',
             photo = 'pic.jpg',
             email = 'gabriel.oduori@gmail.com')
        
        self.project1 = Project(
             title ='testuser',
             description = 'This is great',
             profile = self.profile1,
             pub_date = '12-05-2019',
             image = 'default.jpg',
             website = 'http://www.gabriel.com')
         
         
    def test_instance(self):
        self.assertTrue(isinstance(self.project1, Project))
         
        
        
    def tearDown(self):
        Project.objects.all().delete()

    
    
class ReviewTesCase(TestCase):
    def setUp(self):
        
        self.user1 = User(
            username = 'test1',
            password =  'tehsingpass'
            )
        
        self.profile1 = Profile (
 
             user = self.user1,
             bio = 'This is great',
             photo = 'pic.jpg',
             email = 'gabriel.oduori@gmail.com')
        
        self.project1 = Project(
             title ='testuser',
             description = 'This is great',
             profile = self.profile1,
             pub_date = '12-05-2019',
             image = 'default.jpg',
             website = 'http://www.gabriel.com')
        
        
        self.review1 = Review (
            pub_date = '12-05-2019',
            author = self.profile1,
            project = self.project1,
            body = 'This is a great comment')
                 
    def test_instance(self):
        self.assertTrue(isinstance(self.review1, Review))

    
    