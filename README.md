# Dynamic Inventory Dashboard

Built a dynamic system to optimize inventory management using predictive modeling and real-time analytics.

# Dynamic Inventory Dashboard System

## Overview
The **Dynamic Inventory Dashboard System** is a Python-based solution designed to optimize inventory management for businesses. The system leverages data analytics, predictive modeling, and real-time insights to help businesses reduce stockouts, prevent overstock situations, and improve operational efficiency.

This project includes a modular and scalable pipeline for data ingestion, cleaning, exploratory analysis, predictive modeling, dashboard creation, and automation.

---

## Key Features
- **Data Ingestion**: Extracts inventory data from flat files and SQL databases.
- **Data Cleaning**: Handles missing values, standardizes formats, and normalizes product categories.
- **Exploratory Data Analysis (EDA)**: Visualizes stock levels, demand patterns, and key metrics.
- **Predictive Modeling**: Uses machine learning models to forecast inventory requirements.
- **Dashboard Creation**: Exports real-time insights for visualization in Power BI or Tableau.
- **Automation**: Automates the pipeline to refresh data and predictions periodically.

---

## Directory Structure

```plaintext
project/
│
├── data_ingestion.py            # Handles data loading from flat files and SQL databases
├── data_cleaning.py             # Cleans and preprocesses raw inventory data
├── eda_analysis.py              # Generates visualizations and insights from inventory data
├── predictive_modeling.py       # Trains and applies predictive models for inventory forecasting
├── data_pipeline.py             # Orchestrates the end-to-end inventory management pipeline
├── dashboard_export.py          # Prepares and exports data for dashboards
├── utils.py                     # Provides helper functions for logging, validation, and utility tasks
├── README.md                    # Project documentation
```

# Modules

## 1. data_ingestion.py
- Extracts data from flat files (CSV) and SQL databases.
- Combines data from multiple sources into a single DataFrame.

## 2. data_cleaning.py
- Handles missing values using strategies like mean, median, or drop.
- Standardizes date formats and normalizes categorical columns.

## 3. eda_analysis.py
- Calculates key inventory metrics like turnover rates and restocking thresholds.
- Visualizes stock levels and demand trends over time.

## 4. predictive_modeling.py
- Prepares features and trains predictive models (Random Forest Regressor) for inventory forecasting.
- Predicts future inventory needs based on historical trends and sales data.

## 5. data_pipeline.py
- Automates the entire workflow from data ingestion to predictive modeling.
- Produces a fully processed dataset ready for dashboard integration.

## 6. dashboard_export.py
- Prepares cleaned and modeled data for visualization.
- Exports dashboard-ready datasets for use in Power BI or Tableau.

## 7. utils.py
- Helper functions for logging, validation, and directory management.
- Includes centralized logging for pipeline monitoring.

---

# Contact

For queries or collaboration, feel free to reach out:

- **Name**: Satej Zunjarrao  
- **Email**: zsatej1028@gmail.com
