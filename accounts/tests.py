from django.test import TestCase, Client
from django.urls import reverse

client = Client()

class AuthorCreateTest(TestCase):
    payload = {
        "email":"test@t3.com",
        "password":"",
        "pincode":"123456",
        "phone_number":"1234567890",
        "first_name": "test",
        "last_name": "test"
    }
        
    def test_mandatory_fields(self):
        res = client.post(
            reverse("create-auther"),
            data = {}
        )
        self.assertEqual(res.status_code, 400)
        self.assertTrue("first_name" in res.json())
        self.assertTrue("last_name" in res.json())
        self.assertTrue("email" in res.json())
        self.assertTrue("phone_number" in res.json())
        self.assertTrue("pincode" in res.json())
        self.assertTrue("password" in res.json())

    def test_mandatory_password_validation(self):
        data = self.payload
        res = client.post(
            reverse("create-auther"),
            data = self.payload
        )
        self.assertTrue("password" in res.json())
        data["password"] = "test"
        res = client.post(
            reverse("create-auther"),
            data = self.payload
        )
        self.assertEqual(res.status_code, 400)
        self.assertTrue("password" in res.json())
        data["password"] = "test12345"
        res = client.post(
            reverse("create-auther"),
            data = self.payload
        )
        self.assertEqual(res.status_code, 400)
        self.assertTrue("password" in res.json())
        data["password"] = "Test@123"
        res = client.post(
            reverse("create-auther"),
            data = self.payload
        )
        self.assertEqual(res.status_code, 201)

    def test_pincode_validation(self):
        data = self.payload
        data["pincode"] = 1234
        res = client.post(
            reverse("create-auther"),
            data = self.payload
        )
        self.assertEqual(res.status_code, 400)
        self.assertTrue("pincode" in res.json())
        data["pincode"] = 123456
        res = client.post(
            reverse("create-auther"),
            data = self.payload
        )
        self.assertEqual(res.status_code, 201)
    
    def test_phone_validation(self):
        data = self.payload
        data["phone_number"] = 1234
        res = client.post(
            reverse("create-auther"),
            data = self.payload
        )
        self.assertEqual(res.status_code, 400)
        self.assertTrue("phone_number" in res.json())
        data["phone_number"] = 1234567890
        res = client.post(
            reverse("create-auther"),
            data = self.payload
        )
        self.assertEqual(res.status_code, 201)
