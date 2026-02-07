from __future__ import annotations

from datetime import datetime
from airflow import DAG
from airflow.decorators import task

# DAG = a workflow
with DAG(
    dag_id="example1_hello_airflow",
    start_date=datetime(2025, 1, 1),   # any past date is fine
    schedule=None,                     # run only when you click "Trigger"
    catchup=False,
    tags=["learning", "basics"],
) as dag:

    @task
    def hello():
        print("Hello Airflow! ✅")
        return "Vivek"

    @task
    def greet(name: str):
        print(f"Welcome, {name}! This value came from the previous task via XCom.")

    # dependency: hello runs first, then greet
    greet(hello())