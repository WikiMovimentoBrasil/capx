from django.test import TestCase
from django.contrib.auth.models import User
from user_profile.models import UserProfile


class TestUserProfileModel(TestCase):
    """Test suite for the UserProfile model"""

    def setUp(self):
        # user to be run with the tests
        self.user = User.objects.create(username="testuser")

    def test_user_profile_is_created(self):
        """test that a user profile is created on user create"""
        user_profile = UserProfile.objects.get(user=self.user)
        self.assertIsNotNone(user_profile)