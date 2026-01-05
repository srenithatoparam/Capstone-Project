# Data Flow Explanation
## SuperStore Sales & Business Performance Analytics System

This document explains how data flows through the end-to-end analytics pipeline, from raw ingestion to business dashboards.

---

## 1. Raw Data Source
- SuperStore sales data is stored as CSV files
- Data resides in Databricks Unity Catalog Volume
- Contains order-level sales, profit, discount, and region data

---

## 2. Bronze Layer – Data Ingestion
- Raw CSV files are read using Python and Pandas
- Schema, date, and numeric validations are performed
- No transformations are applied at this stage
- Purpose: Preserve raw data for traceability

---

## 3. Silver Layer – Data Cleaning & Transformation
- Duplicate records are removed
- Missing values are handled
- Date fields are standardized
- Region, Category, and Sub-Category fields are standardized
- Derived metrics like Profit Margin are created
- Cleaned data is stored in Parquet format

---

## 4. Gold Layer – Business Analytics
- PySpark is used for scalable analytics
- Sales and profit trends are calculated
- Category and sub-category performance is analyzed
- Loss-making products are identified
- Regional sales and profitability are computed

---

## 5. Analytics Storage
- Aggregated results are stored as Parquet and CSV
- These datasets act as the single source of truth for reporting

---

## 6. Visualization Layer – Power BI
- Power BI connects to Gold layer outputs
- Dashboards display KPIs, trends, and insights
- Business users consume data for decision-making

---

## 7. Workflow Orchestration
- Apache Airflow orchestrates the pipeline
- Bronze → Silver → Gold execution is automated
- Task dependencies, retries, and logging are implemented

---

## Summary
The structured data flow ensures data accuracy, scalability, and reliable business insights.

---
