from datetime import timedelta
import datetime as dt

from airflow import DAG
from airflow.operators.python import PythonOperator
from sqlalchemy import create_engine, text

engine = create_engine('postgresql://postgres:postgres@db:5432/customers')

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': dt.datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'user_total_spent',
    default_args=default_args,
    description='Calculate total spent by each user and update user_total_spent table',
    schedule_interval=timedelta(minutes=1),
)

def calculate_total_spent():
    conn = engine.connect()
    purchases = conn.execute(text('SELECT customer_id, SUM(price_at_purchase_time) FROM purchases GROUP BY customer_id'))
    for purchase in purchases:
        customer_id, total_spent = purchase
        user_total_spent = conn.execute(text(f'SELECT * FROM user_total_spent WHERE customer_id = {customer_id}')).fetchone()
        if user_total_spent:
            conn.execute(text(f'UPDATE user_total_spent SET total_spent = {total_spent} WHERE customer_id = {customer_id}'))
        else:
            conn.execute(text(f'INSERT INTO user_total_spent (customer_id, total_spent) VALUES ({customer_id}, {total_spent})'))
    conn.close()

t1 = PythonOperator(
    task_id='calculate_total_spent',
    python_callable=calculate_total_spent,
    dag=dag,
)
