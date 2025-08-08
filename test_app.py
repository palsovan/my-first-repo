import unittest
import json
from app import app, db, Order

class OrderManagementTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_order(self):
        response = self.client.post('/orders', json={
            'customer_name': 'John Doe',
            'product_name': 'Widget',
            'quantity': 5
        })
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['customer_name'], 'John Doe')
        self.assertEqual(data['product_name'], 'Widget')
        self.assertEqual(data['quantity'], 5)

    def test_get_orders(self):
        self.client.post('/orders', json={
            'customer_name': 'John Doe',
            'product_name': 'Widget',
            'quantity': 5
        })
        response = self.client.get('/orders')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['customer_name'], 'John Doe')

    def test_get_order(self):
        response = self.client.post('/orders', json={
            'customer_name': 'John Doe',
            'product_name': 'Widget',
            'quantity': 5
        })
        order_id = json.loads(response.data)['id']
        response = self.client.get(f'/orders/{order_id}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['customer_name'], 'John Doe')
        self.assertEqual(data['product_name'], 'Widget')
        self.assertEqual(data['quantity'], 5)

    def test_update_order(self):
        response = self.client.post('/orders', json={
            'customer_name': 'John Doe',
            'product_name': 'Widget',
            'quantity': 5
        })
        order_id = json.loads(response.data)['id']
        response = self.client.put(f'/orders/{order_id}', json={
            'quantity': 10
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['quantity'], 10)

    def test_delete_order(self):
        response = self.client.post('/orders', json={
            'customer_name': 'John Doe',
            'product_name': 'Widget',
            'quantity': 5
        })
        order_id = json.loads(response.data)['id']
        response = self.client.delete(f'/orders/{order_id}')
        self.assertEqual(response.status_code, 204)
        response = self.client.get(f'/orders/{order_id}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()