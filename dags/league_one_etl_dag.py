from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

etl_path = os.path.join(os.path.dirname(__file__), '..', 'etl')
sys.path.insert(0, etl_path)

from league_one_etl import fetch_future_matches, load_to_sqlite

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2026, 1, 29),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'league_one_daily_etl',
    default_args=default_args,
    description='Daily ETL pipeline for upcoming English League One matches',
    schedule_interval='0 8 * * *',  # varje dag kl 08:00
    catchup=False
)


def etl_task():
    matches = fetch_future_matches()  # Extract + Transform
    load_to_sqlite(matches)           

task = PythonOperator(
    task_id='etl_league_one_task',
    python_callable=etl_task,
    dag=dag
)