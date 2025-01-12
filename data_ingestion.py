"""
Module: Data Ingestion
Author: Satej
Description: This module handles data ingestion from multiple sources, including flat files and SQL databases.
"""

import pandas as pd
import sqlalchemy as db

def load_from_csv(file_path):
    """
    Load data from a CSV file into a Pandas DataFrame.
    
    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        # Reading data from CSV file
        data = pd.read_csv(file_path)
        print(f"Data successfully loaded from {file_path}")
        return data
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        raise

def load_from_sql(database_uri, query):
    """
    Load data from an SQL database using a specified query.
    
    Args:
        database_uri (str): The database connection URI.
        query (str): SQL query to fetch data.

    Returns:
        pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        # Establishing connection to the database
        engine = db.create_engine(database_uri)
        with engine.connect() as connection:
            # Executing the SQL query
            data = pd.read_sql_query(query, connection)
        print("Data successfully loaded from SQL database.")
        return data
    except Exception as e:
        print(f"Error loading data from SQL database: {e}")
        raise

if __name__ == "__main__":
    # Example usage
    csv_path = "path/to/inventory_data.csv"  # Replace with the actual path
    sql_uri = "sqlite:///path/to/database.db"  # Replace with the actual database URI
    sql_query = "SELECT * FROM inventory"

    # Load data from CSV
    csv_data = load_from_csv(csv_path)

    # Load data from SQL
    sql_data = load_from_sql(sql_uri, sql_query)
