import os

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base
from database.customer_dal import CustomerDAL
from database.purchase_dal import PurchaseDAL
from database.item_dal import ItemDAL
from api import rest_controller
from database.seeder import DatabaseSeeder
from kafka_consumer.consumer import KafkaPurchaseConsumer
from util.logger import get_logger

app = Flask(__name__)
    
# Get configuration from environment variables
database_url = os.environ['DATABASE_URL']
bootstrap_servers = os.environ['BOOTSTRAP_SERVERS']
topic = os.environ['TOPIC']

logger = get_logger(__name__)

logger.info(f"Starting with config: database_url={database_url}, bootstrap_servers={bootstrap_servers}, topic={topic}")

# Create SQLAlchemy session for interacting with the database
engine = create_engine(database_url)
Session = sessionmaker(bind=engine)
session = Session()

# Create DAL instances to be propagated to their dependant components
customer_dal = CustomerDAL(session=session)
item_dal= ItemDAL(session=session) 
purchase_dal=PurchaseDAL(session=session)

# Handle DDL and seeding
if os.environ.get('STAGE') == 'dev':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    seeder = DatabaseSeeder(customer_dal=customer_dal, item_dal=item_dal, purchase_dal=purchase_dal)
    seeder.run()


# Set up Kafka Consumer and Flask Rest Controller
KafkaPurchaseConsumer(purchase_dal=purchase_dal, topic="purchases", bootstrap_servers=bootstrap_servers)
rest_controller.RestController(app=app, customer_dal=customer_dal)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)



