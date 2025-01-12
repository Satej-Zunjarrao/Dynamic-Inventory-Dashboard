"""
Module: Data Pipeline
Author: Satej
Description: This module automates the end-to-end data pipeline, including data ingestion, cleaning, 
transformation, predictive modeling, and preparing data for dashboard export.
"""

import pandas as pd
from data_ingestion import load_from_csv, load_from_sql
from data_cleaning import handle_missing_values, standardize_date_format, normalize_categories
from predictive_modeling import prepare_features, train_model, predict_inventory

def run_data_pipeline(csv_path, sql_uri, sql_query, feature_columns, target_column, output_path):
    """
    Automate the entire data pipeline from ingestion to data preparation for dashboard export.
    
    Args:
        csv_path (str): Path to the CSV file for ingestion.
        sql_uri (str): Database connection URI for SQL ingestion.
        sql_query (str): SQL query for fetching data.
        feature_columns (list): List of feature columns for predictive modeling.
        target_column (str): The target column for predictive modeling.
        output_path (str): Path to save the processed data.
    
    Returns:
        None
    """
    try:
        # Step 1: Data Ingestion
        print("Starting data ingestion...")
        csv_data = load_from_csv(csv_path)
        sql_data = load_from_sql(sql_uri, sql_query)
        data = pd.concat([csv_data, sql_data], ignore_index=True)
        print("Data ingestion completed.")

        # Step 2: Data Cleaning
        print("Starting data cleaning...")
        data = handle_missing_values(data, strategy="mean", columns=["stock_level", "price"])
        data = standardize_date_format(data, date_column="last_updated")
        data = normalize_categories(data, category_column="product_category")
        print("Data cleaning completed.")

        # Step 3: Predictive Modeling
        print("Starting predictive modeling...")
        X, y = prepare_features(data, target_column=target_column, feature_columns=feature_columns)
        model = train_model(X, y)

        # Generate predictions for the entire dataset
        data["predicted_demand"] = predict_inventory(model, X)
        print("Predictive modeling completed.")

        # Step 4: Export Processed Data
        print(f"Exporting processed data to {output_path}...")
        data.to_csv(output_path, index=False)
        print(f"Data pipeline executed successfully. Processed data saved to {output_path}.")

    except Exception as e:
        print(f"Error in data pipeline: {e}")
        raise

if __name__ == "__main__":
    # Example usage
    csv_path = "path/to/inventory_data.csv"  # Replace with actual path
    sql_uri = "sqlite:///path/to/database.db"  # Replace with actual SQL URI
    sql_query = "SELECT * FROM inventory"
    feature_columns = ["stock_level", "sales", "reorder_point"]
    target_column = "future_demand"
    output_path = "path/to/processed_data.csv"  # Replace with actual output path

    run_data_pipeline(csv_path, sql_uri, sql_query, feature_columns, target_column, output_path)
