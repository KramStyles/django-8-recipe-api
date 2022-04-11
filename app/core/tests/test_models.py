from django.test import TestCase
from django.contrib.auth import get_user_model


class TestModels(TestCase):
    def setUp(self):
        self.email = 'me@email.com'
        self.password = '1234pass'

    def test_if_user_creates_with_email(self):
        """Test to check if an account can be created with an email address"""
        user = get_user_model().objects.create_user(email=self.email, password=self.password)

        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))

    def test_to_normalize_email_address(self):
        """Test if email address is case-insensitive"""
        user = get_user_model().objects.create_user(self.email.upper(), self.password)
        self.assertEqual(user.email, self.email)

    def test_to_check_if_email_was_provided(self):
        """Test to check if email address was provided"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None)

    def test_to_create_super_user(self):
        user = get_user_model().objects.create_superuser(self.email, self.password)

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
