from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from .models import FoodItem, Order, Seller

User = get_user_model()
REG = {"username": "bob", "password": "S3cure-pass-99", "first_name": "Bob",
       "email": "b@x.com", "phone": "0821234567"}
SHIP = {"contact_name": "Bob", "contact_phone": "0821234567", "delivery_address": "Res 4"}


class ApiTests(APITestCase):
    def setUp(self):
        self.su = User.objects.create_user("seller1", password="pw-12345-x")
        self.s1 = Seller.objects.create(name="Mama Thandi", faculty="Science",
                                        phone="0829998888", user=self.su)
        self.s2 = Seller.objects.create(name="Kota King", faculty="Law")
        self.f1 = FoodItem.objects.create(seller=self.s1, name="Pap", price="20.00")
        self.f2 = FoodItem.objects.create(seller=self.s2, name="Kota", price="35.00")

    def login_customer(self):
        r = self.client.post("/api/auth/register/", REG, format="json")
        self.assertEqual(r.status_code, 201)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + r.data["token"])

    def test_public_catalogue_hides_phone_and_scopes_food(self):
        r = self.client.get("/api/sellers/")
        self.assertEqual(len(r.data), 2)
        self.assertNotIn("phone", r.data[0])
        foods = self.client.get(f"/api/sellers/{self.s1.pk}/foods/").data
        self.assertEqual([f["name"] for f in foods], ["Pap"])

    def test_checkout_needs_login_and_splits_by_seller(self):
        body = {**SHIP, "items": [{"food": self.f1.pk, "quantity": 2},
                                  {"food": self.f2.pk, "quantity": 1}]}
        self.assertEqual(self.client.post("/api/orders/", body, format="json").status_code, 401)
        self.login_customer()
        r = self.client.post("/api/orders/", body, format="json")
        self.assertEqual(r.status_code, 201)
        self.assertEqual(len(r.data), 2)
        self.assertEqual(Order.objects.get(seller=self.s1).total, 40)

    def test_unavailable_food_rejected(self):
        self.login_customer()
        self.f1.is_available = False
        self.f1.save()
        r = self.client.post("/api/orders/", {**SHIP, "items": [{"food": self.f1.pk, "quantity": 1}]},
                             format="json")
        self.assertEqual(r.status_code, 400)

    def test_mutual_contact_reveal(self):
        self.login_customer()
        r = self.client.post("/api/orders/", {**SHIP, "items": [{"food": self.f1.pk, "quantity": 1}]},
                             format="json")
        oid = r.data[0]["id"]
        self.assertIsNone(r.data[0]["seller_contact"])

        cust_auth = self.client._credentials
        self.client.credentials()
        tok = self.client.post("/api/auth/login/", {"username": "seller1", "password": "pw-12345-x"},
                               format="json").data["token"]
        self.client.credentials(HTTP_AUTHORIZATION="Token " + tok)
        self.assertIsNone(self.client.get("/api/seller/orders/").data[0]["customer_contact"])
        self.assertEqual(self.client.post(f"/api/seller/orders/{oid}/approve/").status_code, 200)
        self.assertEqual(self.client.get("/api/seller/orders/").data[0]["customer_contact"]["phone"],
                         "0821234567")

        self.client.credentials(**cust_auth)
        mine = self.client.get("/api/orders/").data[0]
        self.assertEqual(mine["seller_contact"]["phone"], "0829998888")

    def test_customer_cannot_use_seller_endpoints(self):
        self.login_customer()
        self.assertEqual(self.client.get("/api/seller/orders/").status_code, 403)

    def test_seller_manages_only_own_food(self):
        self.client.force_authenticate(self.su)
        r = self.client.post("/api/seller/foods/", {"name": "Vetkoek", "price": "12.50"}, format="multipart")
        self.assertEqual(r.status_code, 201)
        self.assertEqual(self.s1.foods.count(), 2)
        self.assertEqual(self.client.patch(f"/api/seller/foods/{self.f2.pk}/", {"name": "x"}).status_code, 404)
