"""
Module: Data Cleaning
Author: Satej
Description: This module handles data cleaning and preprocessing tasks such as handling missing values, 
standardizing date formats, and normalizing product categories.
"""

import pandas as pd

def handle_missing_values(data, strategy="mean", columns=None):
    """
    Handle missing values in the dataset based on the specified strategy.
    
    Args:
        data (pd.DataFrame): The input DataFrame.
        strategy (str): Strategy to handle missing values ('mean', 'median', 'drop').
        columns (list): List of columns to apply the strategy. If None, applies to all numeric columns.
    
    Returns:
        pd.DataFrame: DataFrame with missing values handled.
    """
    try:
        if strategy == "mean":
            data[columns] = data[columns].fillna(data[columns].mean())
        elif strategy == "median":
            data[columns] = data[columns].fillna(data[columns].median())
        elif strategy == "drop":
            data = data.dropna(subset=columns)
        else:
            raise ValueError("Invalid strategy specified. Use 'mean', 'median', or 'drop'.")
        print(f"Missing values handled using strategy: {strategy}")
        return data
    except Exception as e:
        print(f"Error handling missing values: {e}")
        raise

def standardize_date_format(data, date_column, target_format="%Y-%m-%d"):
    """
    Standardize the format of a date column in the dataset.
    
    Args:
        data (pd.DataFrame): The input DataFrame.
        date_column (str): Name of the date column.
        target_format (str): Desired date format (default: '%Y-%m-%d').
    
    Returns:
        pd.DataFrame: DataFrame with standardized date column.
    """
    try:
        data[date_column] = pd.to_datetime(data[date_column]).dt.strftime(target_format)
        print(f"Date column '{date_column}' standardized to format {target_format}")
        return data
    except Exception as e:
        print(f"Error standardizing date column '{date_column}': {e}")
        raise

def normalize_categories(data, category_column):
    """
    Normalize the values in a categorical column by converting them to lowercase.
    
    Args:
        data (pd.DataFrame): The input DataFrame.
        category_column (str): Name of the categorical column.
    
    Returns:
        pd.DataFrame: DataFrame with normalized categorical column.
    """
    try:
        data[category_column] = data[category_column].str.lower()
        print(f"Categorical column '{category_column}' normalized.")
        return data
    except Exception as e:
        print(f"Error normalizing categorical column '{category_column}': {e}")
        raise

if __name__ == "__main__":
    # Example usage
    file_path = "path/to/inventory_data.csv"  # Replace with the actual path
    data = pd.read_csv(file_path)

    # Handle missing values
    cleaned_data = handle_missing_values(data, strategy="mean", columns=["stock_level", "price"])

    # Standardize date format
    cleaned_data = standardize_date_format(cleaned_data, date_column="last_updated")

    # Normalize product categories
    cleaned_data = normalize_categories(cleaned_data, category_column="product_category")
