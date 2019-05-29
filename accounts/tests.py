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
        


        

# class ProfileTestClass(TestCase):
#     def setUp(self):
#         #  Creating a new editor and saving it
#          self.profile1 = Profile(
#              user.user1 ='test1',
#              bio = 'This is great',
#              photo = 'pic.jpg',
#              email = 'gabriel.oduori@gmail.com')
#     def test_instance(self):
#         self.assertTrue(isinstance(self.profile1, Profile))
         
         
#         # Testing Save Method
#     def test_save_method(self):
#         self.profile1.save_profile()
#         profiles = Profile.objects.all()
#         self.assertTrue(len(profiles) > 0)

        
        