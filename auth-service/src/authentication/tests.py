from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase

User = get_user_model()


class TokenTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="user", is_active=True)
        self.user.set_password("password")
        self.user.save()

    def test_obtain_token_pair(self):
        response = self.client.post(
            reverse("token_obtain_pair"),
            {"username": self.user.username, "password": "password"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "refresh",
        )
        self.assertContains(response, "access")
