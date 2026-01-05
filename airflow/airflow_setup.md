# Apache Airflow Setup Guide  
## SuperStore Sales & Business Performance Analytics System

This document explains how Apache Airflow is used in this project to orchestrate the end-to-end ETL pipeline following industry best practices.

---

## Why Apache Airflow?

Apache Airflow is used to:

- Automate the end-to-end ETL workflow  
- Schedule daily execution of data pipelines  
- Manage task dependencies (Bronze → Silver → Gold)  
- Handle retries and failures gracefully  
- Track pipeline execution using logs  

This satisfies the **Workflow Automation** requirement of the capstone project.

---

## ETL Pipeline Architecture

Raw CSV Files
↓
Bronze Layer – Data Ingestion
↓
Silver Layer – Cleaning & Transformation
↓
Gold Layer – Business Analytics
↓
Power BI Dashboards

Airflow orchestrates the **Bronze → Silver → Gold** pipeline.

---

## DAG Overview

- **DAG Name:** `superstore_sales_etl_pipeline`
- **Schedule:** Daily (`@daily`)
- **Start Date:** 2024-01-01
- **Retries:** 2
- **Retry Delay:** 5 minutes
- **Catchup:** Disabled

---

## DAG Tasks Explained

### 🔹 Task 1: Bronze Ingestion
- Reads raw SuperStore CSV files  
- Validates schema, date, and numeric fields  
- Logs ingestion status  

### 🔹 Task 2: Silver Transformation
- Cleans and standardizes data  
- Handles missing values and duplicates  
- Creates derived metrics such as profit margin  

### 🔹 Task 3: Gold Analytics
- Generates business KPIs  
- Identifies loss-making products  
- Creates category-wise and regional analytics  

---

## Task Dependencies

Bronze Ingestion
↓
Silver Transformation
↓
Gold Analytics


Each task executes only after the previous task completes successfully.

---

## Retry & Failure Handling

- Each task is configured with:
  - `retries = 2`
  - `retry_delay = 5 minutes`
- Automatic retries ensure pipeline reliability
- Failures are captured through task logs

---

## Logging & Monitoring

- Airflow captures logs for each task execution
- Logs help with:
  - Debugging failures
  - Auditing pipeline runs
  - Monitoring ETL health

---

## How the DAG is Executed

### Option 1: Local / WSL

```bash
airflow db migrate
airflow webserver
airflow scheduler
```

### Option 2: Databricks-Orchestrated Execution

- Airflow DAG triggers Databricks notebooks
- Databricks Jobs UI displays pipeline graph
- Provides scalable execution and monitoring

## Summary

Apache Airflow acts as the workflow backbone of this project by:

- Ensuring automated execution
- Managing task dependencies
- Providing production-grade monitoring
- This completes the Workflow Automation module of the capstone project.