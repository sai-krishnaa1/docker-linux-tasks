import sys
import os
import logging
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
 
# Append scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scripts'))
 
# Import preprocessing scripts
from merge_data import merge_data
from clean_data import clean_data
from split_data import split_data
from transform_data import transform_data
 
# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
 
# Default DAG arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 2, 12),  # Adjust start date as needed
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
 
# DAG Definition
with DAG(
    dag_id='titanic_preprocessing',
    default_args=default_args,
    schedule_interval='@daily',  # Run daily
    catchup=False
) as dag:
 
    # Task 1: Merge Data
    merge_task = PythonOperator(
        task_id='merge_data',
        python_callable=merge_data,
        op_kwargs={'data_path': '/opt/airflow/data'}
    )
 
    # Task 2: Clean Data
    clean_task = PythonOperator(
        task_id='clean_data',
        python_callable=clean_data,
        op_kwargs={'data_path': '/opt/airflow/data'}
    )
 
    # Task 3: Split Data
    split_task = PythonOperator(
        task_id='split_data',
        python_callable=split_data,
        op_kwargs={'data_path': '/opt/airflow/data'}
    )
 
    # Task 4: Transform Data (OHE)
    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
        op_kwargs={'data_path': '/opt/airflow/data'}
    )
 
    # Define Task Dependencies
    merge_task >> clean_task >> split_task >> transform_task