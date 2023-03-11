from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base, Customer, Item
from database.purchase_dal import PurchaseDAL


class TestPurchaseDAL(TestCase):
    def setUp(self):
        engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.purchase_dal = PurchaseDAL(session=self.session)

        # Create a customer and an item to use in tests
        self.customer = Customer(name='John Doe')
        self.item = Item(name='Test Item', price=9.99)
        self.session.add_all([self.customer, self.item])
        self.session.commit()

    def tearDown(self):
        self.session.close()

    def test_create_purchase(self):
        # Test that a new purchase can be created
        customer_id = self.customer.id
        item_id = self.item.id
        purchase = self.purchase_dal.create_purchase(customer_id=customer_id, item_id=item_id)
        self.assertIsNotNone(purchase.id)
        self.assertEqual(purchase.customer_id, customer_id)
        self.assertEqual(purchase.item_id, item_id)
        self.assertEqual(purchase.price_at_purchase_time, self.item.price)
