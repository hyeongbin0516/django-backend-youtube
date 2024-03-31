from django.test import TestCase
from django.contrib.auth import get_user_model

class UserTestCase(TestCase):
    # 회원가입(가정)
    def test_create_user(self):
        email = 'hyeongbin7169@daum.net'
        password = 'password123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        email = 'hyeongbin7169@daum.net'
        password = 'password123'

        super_user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
            

        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
