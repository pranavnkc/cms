from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from django.urls import reverse
from .models import Content

client = APIClient()


class AuthorCreateTest(TestCase):

    def test_content_list_access(self):
        author1 = {
            "email": "auther1@gmail.com",
            "password": "Test@123",
            "pincode": "123456",
            "phone_number": "1234567890",
            "first_name": "test",
            "last_name": "test"
        }
        author2 = {
            "email": "auther2@gmail.com",
            "password": "Test@123",
            "pincode": "123456",
            "phone_number": "1234567890",
            "first_name": "test",
            "last_name": "test"
        }
        self.author1 = client.post(
            reverse("create-auther"),
            data=author1
        ).json()
        self.author2 = client.post(
            reverse("create-auther"),
            data=author2
        ).json()
        self.auther1_token = client.post(
            reverse("api_token_auth"),
            data={
                "username": author1["email"],
                "password": author1["password"],
            }
        ).json()
        self.auther2_token = client.post(
            reverse("api_token_auth"),
            data={
                "username": author2["email"],
                "password": author2["password"],
            }
        ).json()
        self.author_1_content = Content.objects.create(**{
            "title": "Author 1 content",
            "body": "Author 1 content",
            "categories": ["test", "test1"],
            "summary": "test",
            "author_id": self.author1["id"]
        })
        self.author_2_content = Content.objects.create(**{
            "title": "Author 1 content",
            "body": "Author 1 content",
            "categories": ["test", "test1"],
            "summary": "test",
            "author_id": self.author2["id"]
        })
        client.credentials(HTTP_AUTHORIZATION='Token ' +
                           self.auther1_token["token"])
        self.assertTrue(self.author_2_content.id not in [row["id"] for row in client.get(
            reverse("content-list"),
        ).json()])
        client.credentials(HTTP_AUTHORIZATION='Token ' +
                           self.auther2_token["token"])
        self.assertTrue(self.author_2_content.id in [row["id"] for row in client.get(
            reverse("content-list"),
        ).json()])
        self.check_auther_can_edit_only_their_content()

    def check_auther_can_edit_only_their_content(self):
        client.credentials(HTTP_AUTHORIZATION='Token ' +
                           self.auther1_token["token"])
        self.assertEqual(client.get(
            reverse("content-detail", args=[self.author_2_content.id])
        ).status_code, 404)
        client.credentials(HTTP_AUTHORIZATION='Token ' +
                           self.auther2_token["token"])
        self.assertEqual(client.get(
            reverse("content-detail", args=[self.author_2_content.id])
        ).status_code, 200)
