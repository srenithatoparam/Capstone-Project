# 🛒 SuperStore Sales & Business Performance Analytics System

An **end-to-end Data Analytics & Data Engineering Capstone Project** built using  
**Python, Pandas, Databricks, PySpark, Apache Airflow, and Power BI**

---

## Business Context

A large retail SuperStore operates across multiple regions and sells products in categories such as **Furniture, Office Supplies, and Technology**.

### Business Challenges
- Sales data stored in multiple raw CSV files
- Manual reporting is time-consuming and error-prone
- Limited visibility into profit, discounts, and regional performance
- Difficulty identifying loss-making products and regions

### Business Need
Build a **centralized, automated analytics system** that:
- Automates sales data processing
- Tracks sales, profit, and discount patterns
- Identifies high-performing and underperforming products
- Provides clear dashboards for business decision-makers

---

## Project Objective

To design and implement an **end-to-end retail analytics solution** that:
- Uses **Python & Pandas** for data ingestion and preprocessing
- Applies **Pandas & PySpark** for analytics and KPI creation
- Uses **Databricks** for scalable data processing
- Orchestrates workflows using **Apache Airflow**
- Visualizes insights using **Power BI**
- Demonstrates **real-world Data Engineering practices**

---

## Architecture Overview

This project follows a **Medallion Architecture**:

Raw CSV → Bronze → Silver → Gold → Power BI

Refer to `docs/architecture_diagram.png`

---

## Technology Stack

- Python, Pandas, NumPy  
- Databricks, PySpark  
- Apache Airflow  
- CSV / Parquet  
- Power BI  
- Git & GitHub  

---

## Project Implementation Steps

### 1️. Data Ingestion (Bronze Layer)
- Loaded raw CSV files using Python & Pandas
- Validated schema, date, and numeric fields
- Logged ingestion status

### 2️. Data Cleaning & Transformation (Silver Layer)
- Removed duplicates
- Handled missing values
- Standardized categories, regions, and dates
- Created derived metrics like profit margin

### 3️. Business Analytics (Gold Layer)
- Sales & profit trends over time
- Category and sub-category performance
- Regional sales & profitability
- Loss-making products identification

### 4️. Workflow Automation (Apache Airflow)
- Created scheduled DAG
- Implemented task dependencies
- Added retries and logging

### 5️. Visualization & Reporting (Power BI)
- Sales & Profit dashboards
- Category-wise and region-wise analysis
- Risk & loss analysis dashboards

### 6️. Testing & Validation
- Spark vs Power BI value validation
- Sales & profit consistency checks
- Dashboard verification

---

## Project Folder Structure

Refer to the project repository structure for:
- ETL scripts
- Databricks notebooks
- Airflow DAGs
- Power BI dashboards
- Documentation files

---

## Dashboards & Business Insights (Power BI)

Four interactive **Power BI dashboards** were built using the Gold layer data to provide clear, actionable insights for business stakeholders and management.

---

### 🔹 Dashboard 1: Sales & Profit Overview
**Purpose:** Track overall business performance at a high level.

**Key Metrics & Visuals:**
- Total Sales, Total Profit, Profit Margin (KPI Cards)
- Monthly Sales & Profit Trends
- Category-wise Sales Performance
- Region-wise Sales Distribution

**Business Impact:**
- Helps management understand overall revenue and profitability trends
- Identifies top-performing categories and regions

---

### 🔹 Dashboard 2: Category & Sub-Category Performance
**Purpose:** Analyze product-level contribution to sales and profit.

**Key Metrics & Visuals:**
- Sales and Profit by Category
- Sub-Category-wise Profitability Analysis
- Contribution of each sub-category to total revenue

**Business Impact:**
- Identifies high-performing and underperforming product segments
- Supports product portfolio optimization decisions

---

### 🔹 Dashboard 3: Regional Performance Analysis
**Purpose:** Compare performance across different regions.

**Key Metrics & Visuals:**
- Sales by Region
- Profit by Region
- Regional Contribution to Total Sales

**Business Impact:**
- Highlights strong and weak regional markets
- Helps in region-specific sales and marketing strategy planning

---

### 🔹 Dashboard 4: Risk & Loss Analysis
**Purpose:** Detect profitability risks and loss drivers.

**Key Metrics & Visuals:**
- Loss-making Products and Sub-Categories
- Discount vs Profit Impact Analysis
- High-discount, Low-profit Identification

**Business Impact:**
- Identifies products causing revenue leakage
- Supports better discounting and pricing strategies

---

### Dashboard Validation
- All dashboard KPIs were cross-verified with **Databricks Spark aggregations**
- Ensured **data accuracy and consistency** across the analytics pipeline

📂 Power BI dashboards and screenshots are available in the `powerbi/` directory.

---

## Key Business Insights

- Technology category drives highest sales
- Discounts significantly impact profit margins
- Certain sub-categories consistently generate losses
- Regional performance varies significantly

---

## Conclusion

This project demonstrates a **production-ready, end-to-end analytics pipeline** with automation, scalability, validation, and business-focused insights.

---

## Author
**Srenitha Toparam**  
Data Engineer | Analytics Enthusiast
