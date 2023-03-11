from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base, Customer, Item, Purchase
from database.customer_dal import CustomerDAL
from database.item_dal import ItemDAL
from database.purchase_dal import PurchaseDAL


class TestCustomerDAL(TestCase):
    def setUp(self):
        engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.customer_dal = CustomerDAL(session=self.session)
        self.item_dal = ItemDAL(session=self.session)
        self.purchase_dal = PurchaseDAL(session=self.session)

        # create test data
        customer = self.customer_dal.create_customer(name='John Doe')
        item1 = self.item_dal.create_item(name='item1', price=100.0)
        item2 = self.item_dal.create_item(name='item2', price=200.0)
        self.purchase_dal.create_purchase(customer_id=customer.id, item_id=item1.id)
        self.purchase_dal.create_purchase(customer_id=customer.id, item_id=item2.id)

    def tearDown(self):
        self.session.close()

    def test_get_customer_purchases(self):
        customer = self.customer_dal.get_customer_by_id(customer_id=1)
        purchases = self.customer_dal.get_customer_purchases(customer_id=customer.id)

        self.assertEqual(len(purchases), 2)
        self.assertEqual(purchases[0].item.name, 'item1')
        self.assertEqual(purchases[0].price_at_purchase_time, 100.0)
        self.assertEqual(purchases[1].item.name, 'item2')
        self.assertEqual(purchases[1].price_at_purchase_time, 200.0)
