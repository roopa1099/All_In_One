from __future__ import annotations

import os
import csv
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


# ---------- Python functions for PythonOperator ----------
def make_sample_csv(**context):
    """
    Creates a small CSV file to act as our sample data.

    We use context to read:
    - ds: run date string like 2026-02-07
    - run_id: unique id for the run
    - params: values defined in DAG params
    - dag_run.conf: values passed when triggering with JSON
    """
    ds = context["ds"]                # e.g., "2026-02-07"
    run_id = context["run_id"]        # e.g., "manual__2026-02-07T..."
    params = context["params"]        # DAG params
    dag_run = context.get("dag_run")  # present for triggered runs

    # Priority: dag_run.conf overrides params (if provided)
    conf = dag_run.conf if dag_run else {}
    rows = int(conf.get("rows", params["rows"]))
    base_value = int(conf.get("base_value", params["base_value"]))

    out_dir = "/tmp/airflow_demo"
    os.makedirs(out_dir, exist_ok=True)

    file_path = f"{out_dir}/sales_{ds}.csv"

    # Create deterministic sample data
    # id, amount
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "amount"])
        for i in range(1, rows + 1):
            writer.writerow([i, base_value * i])

    print("✅ Created file:", file_path)
    print("Run ID:", run_id)
    print("Rows:", rows, "Base value:", base_value)

    # Return file_path -> will be stored in XCom automatically by PythonOperator? (No, not by default)
    # So we'll push to XCom ourselves:
    context["ti"].xcom_push(key="file_path", value=file_path)


def summarize_csv(**context):
    """
    Reads the CSV file created earlier and prints simple summary stats.
    """
    ti = context["ti"]
    file_path = ti.xcom_pull(task_ids="make_csv", key="file_path")

    if not file_path or not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file not found: {file_path}")

    row_count = 0
    total_amount = 0

    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row_count += 1
            total_amount += int(row["amount"])

    print("✅ Summary")
    print("File:", file_path)
    print("Row count:", row_count)
    print("Total amount:", total_amount)


# ---------- DAG definition ----------
default_args = {
    "owner": "vivek",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="example2_bash_python_params",
    description="Example 2: BashOperator + PythonOperator + params + templating",
    start_date=datetime(2025, 1, 1),
    schedule=None,       # run only when triggered
    catchup=False,
    default_args=default_args,
    tags=["learning", "basics"],
    params={
        "rows": 5,        # default rows if you don’t override during trigger
        "base_value": 10  # amounts will be 10,20,30,...
    },
) as dag:

    make_csv = PythonOperator(
        task_id="make_csv",
        python_callable=make_sample_csv,
    )

    preview_file = BashOperator(
        task_id="preview_file",
        # Jinja templating is supported inside bash_command.
        # We will read the file path from XCom using a template expression.
        bash_command="""
        echo "Run date (ds): {{ ds }}"
        echo "Run id: {{ run_id }}"
        echo "Rows param (default): {{ params.rows }}"
        echo "Base value param (default): {{ params.base_value }}"
        echo "CSV path from XCom: {{ ti.xcom_pull(task_ids='make_csv', key='file_path') }}"
        echo "---- File Preview ----"
        head -n 6 {{ ti.xcom_pull(task_ids='make_csv', key='file_path') }}
        """,
    )

    summarize = PythonOperator(
        task_id="summarize_csv",
        python_callable=summarize_csv,
    )

    # dependencies
    make_csv >> preview_file >> summarize