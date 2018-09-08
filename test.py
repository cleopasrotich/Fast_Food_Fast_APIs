import unittest
from app import orders, app


class Testapp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client

    def test_get_all(self):
        response = self.client().get('http://localhost:5000/Fast_Food_Fast/api/v1/orders')
        self.assertEqual(orders, response.data)

    def test_get_one(self):
        response = self.client().get('http://localhost:5000/Fast_Food_Fast/api/v1/orders/4')
        self.assertEqual(orders, response.data)

    def test_get_post(self):
        response = self.client().post('/Fast_Food_Fast/api/v1/orders')
        self.assertEqual(orders, response.data)
