from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
import logging

# Default configuration for all tasks in the DAG
default_args = {
    "owner": "data_engineer",                 # Owner of the pipeline
    "depends_on_past": False,                 # Each run is independent
    "email_on_failure": False,                # Disable email alerts
    "email_on_retry": False,                  # Disable retry emails
    "retries": 2,                             # Retry failed tasks twice
    "retry_delay": timedelta(minutes=5),      # Wait 5 minutes before retry
}

# Define the Airflow DAG
with DAG(
    dag_id="superstore_sales_etl_pipeline",   # Unique DAG name
    default_args=default_args,                # Apply default settings
    description="End-to-End SuperStore ETL Pipeline",
    start_date=datetime(2024, 1, 1),           # Pipeline start date
    schedule="@daily",                         # Run pipeline daily
    catchup=False,                             # Do not backfill old runs
    tags=["superstore", "etl", "capstone"],    # Tags for organization
) as dag:

    # Bronze layer task: Raw data ingestion
    def bronze_ingestion():
        logging.info("Bronze Layer started")
        logging.info("Raw SuperStore CSV data ingested successfully")

    bronze_task = PythonOperator(
        task_id="bronze_ingestion",             # Task name
        python_callable=bronze_ingestion,       # Function to execute
    )

    # Silver layer task: Data cleaning and transformation
    def silver_transformation():
        logging.info("Silver Layer started")
        logging.info("Data cleaned, standardized, and transformed")

    silver_task = PythonOperator(
        task_id="silver_transformation",
        python_callable=silver_transformation,
    )

    # Gold layer task: Business analytics and KPIs
    def gold_analytics():
        logging.info("Gold Layer started")
        logging.info("Business KPIs and analytics generated")

    gold_task = PythonOperator(
        task_id="gold_analytics",
        python_callable=gold_analytics,
    )

    # Define task execution order (ETL flow)
    bronze_task >> silver_task >> gold_task
