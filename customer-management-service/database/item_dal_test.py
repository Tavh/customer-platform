from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base
from database.item_dal import ItemDAL


class TestItemDAL(TestCase):
    def setUp(self):
        engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.item_dal = ItemDAL(session=self.session)

    def tearDown(self):
        self.session.close()

    def test_create_item(self):
        # Test that a new item can be created
        item_name = 'Widget'
        item_price = 9.99
        item = self.item_dal.create_item(name=item_name, price=item_price)
        self.assertIsNotNone(item.id)
        self.assertEqual(item.name, item_name)
        self.assertEqual(item.price, item_price)

    def test_get_item_by_id(self):
        # Test that an item can be retrieved by its ID
        item_name = 'Widget'
        item_price = 9.99
        item = self.item_dal.create_item(name=item_name, price=item_price)
        retrieved_item = self.item_dal.get_item_by_id(item_id=item.id)
        self.assertEqual(retrieved_item, item)

