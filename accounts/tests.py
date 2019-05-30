from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.


class UserTestClass(TestCase):

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

    def test_instance(self):
        self.assertTrue(isinstance(self.user1, User))
        
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile1, Profile))
        



        
        