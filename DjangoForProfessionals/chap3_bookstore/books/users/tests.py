
from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

class CustomerTests(TestCase):
    def test_create_user(self):
        user =  User.objects.create_user(
            username = 'will',
            email = 'will.gmail.com',
            password='testpass123'
        )

        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@gmail.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertFalse(user.is_superuser)
        )




