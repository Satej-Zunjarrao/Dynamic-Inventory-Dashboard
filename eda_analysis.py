"""
Module: Exploratory Data Analysis (EDA)
Author: Satej
Description: This module performs in-depth exploratory data analysis (EDA) on inventory data 
to identify trends, calculate metrics, and generate visualizations.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_inventory_metrics(data):
    """
    Calculate key inventory metrics such as turnover rates and restocking thresholds.
    
    Args:
        data (pd.DataFrame): The input DataFrame containing inventory data.

    Returns:
        dict: A dictionary with calculated metrics.
    """
    try:
        turnover_rate = (data["sales"] / data["stock_level"]).mean()
        restocking_threshold = data["stock_level"].quantile(0.2)  # 20th percentile
        metrics = {
            "turnover_rate": turnover_rate,
            "restocking_threshold": restocking_threshold,
        }
        print("Inventory metrics calculated successfully.")
        return metrics
    except Exception as e:
        print(f"Error calculating inventory metrics: {e}")
        raise

def plot_stock_levels(data, product_column, stock_column):
    """
    Generate a visualization of stock levels over time for each product.
    
    Args:
        data (pd.DataFrame): The input DataFrame.
        product_column (str): Name of the product identifier column.
        stock_column (str): Name of the stock level column.
    
    Returns:
        None
    """
    try:
        grouped_data = data.groupby(product_column)[stock_column].mean()
        grouped_data.plot(kind="bar", figsize=(10, 6))
        plt.title("Average Stock Levels by Product")
        plt.xlabel("Product")
        plt.ylabel("Average Stock Level")
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error generating stock level plot: {e}")
        raise

def analyze_demand_patterns(data, date_column, sales_column):
    """
    Analyze demand patterns by visualizing sales trends over time.
    
    Args:
        data (pd.DataFrame): The input DataFrame.
        date_column (str): Name of the date column.
        sales_column (str): Name of the sales column.
    
    Returns:
        None
    """
    try:
        data[date_column] = pd.to_datetime(data[date_column])
        daily_sales = data.groupby(date_column)[sales_column].sum()
        daily_sales.plot(figsize=(12, 6))
        plt.title("Daily Sales Trends")
        plt.xlabel("Date")
        plt.ylabel("Total Sales")
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error analyzing demand patterns: {e}")
        raise

if __name__ == "__main__":
    # Example usage
    file_path = "path/to/inventory_data.csv"  # Replace with the actual path
    data = pd.read_csv(file_path)

    # Calculate metrics
    metrics = calculate_inventory_metrics(data)
    print(metrics)

    # Plot stock levels
    plot_stock_levels(data, product_column="product_id", stock_column="stock_level")

    # Analyze demand patterns
    analyze_demand_patterns(data, date_column="date", sales_column="sales")
