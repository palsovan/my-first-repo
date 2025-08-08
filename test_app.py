import unittest
from app import app, db, Bill

class TestApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Billing App', response.data)

    def test_add_bill(self):
        response = self.app.post('/add_bill', data=dict(
            customer_name='Test Customer',
            amount='100.50'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Customer', response.data)
        self.assertIn(b'100.50', response.data)

    def test_bill_model(self):
        with app.app_context():
            bill = Bill(customer_name='Test Customer', amount=100.50)
            db.session.add(bill)
            db.session.commit()
            retrieved_bill = Bill.query.filter_by(customer_name='Test Customer').first()
            self.assertIsNotNone(retrieved_bill)
            self.assertEqual(retrieved_bill.amount, 100.50)

if __name__ == '__main__':
    unittest.main()