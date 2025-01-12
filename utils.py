"""
Module: Utility Functions
Author: Satej
Description: This module contains helper functions for common tasks such as logging, configuration management,
data validation, and error handling. These functions are designed to be reusable across the project.
"""

import os
import logging
import pandas as pd
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="logs/project_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_message(message, level="info"):
    """
    Log a message to the project log file.
    
    Args:
        message (str): The message to log.
        level (str): The severity level ('info', 'warning', 'error').
    
    Returns:
        None
    """
    try:
        if level == "info":
            logging.info(message)
        elif level == "warning":
            logging.warning(message)
        elif level == "error":
            logging.error(message)
        else:
            raise ValueError("Invalid logging level specified.")
    except Exception as e:
        print(f"Error in logging message: {e}")
        raise

def validate_file_path(file_path):
    """
    Validate if the given file path exists.
    
    Args:
        file_path (str): The path to the file.
    
    Returns:
        bool: True if the file exists, False otherwise.
    """
    try:
        if os.path.exists(file_path):
            return True
        else:
            log_message(f"File not found: {file_path}", level="warning")
            return False
    except Exception as e:
        log_message(f"Error validating file path: {e}", level="error")
        raise

def validate_dataframe(df, required_columns):
    """
    Validate if a DataFrame contains the required columns.
    
    Args:
        df (pd.DataFrame): The DataFrame to validate.
        required_columns (list): List of required column names.
    
    Returns:
        bool: True if all required columns are present, False otherwise.
    """
    try:
        missing_columns = [col for col in required_columns if col not in df.columns]
        if not missing_columns:
            return True
        else:
            log_message(f"Missing columns in DataFrame: {missing_columns}", level="warning")
            return False
    except Exception as e:
        log_message(f"Error validating DataFrame: {e}", level="error")
        raise

def get_current_timestamp():
    """
    Get the current timestamp in a readable format.
    
    Returns:
        str: The current timestamp as a string.
    """
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return timestamp
    except Exception as e:
        log_message(f"Error generating timestamp: {e}", level="error")
        raise

def create_directory(dir_path):
    """
    Create a directory if it does not exist.
    
    Args:
        dir_path (str): The path to the directory to create.
    
    Returns:
        None
    """
    try:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            log_message(f"Directory created: {dir_path}")
        else:
            log_message(f"Directory already exists: {dir_path}")
    except Exception as e:
        log_message(f"Error creating directory: {e}", level="error")
        raise

if __name__ == "__main__":
    # Example usage

    # Validate file path
    test_file_path = "path/to/inventory_data.csv"  # Replace with an actual path
    if validate_file_path(test_file_path):
        log_message(f"Validated file path: {test_file_path}")

    # Validate DataFrame columns
    sample_data = {
        "product_id": [1, 2, 3],
        "stock_level": [50, 30, 20],
        "price": [100, 150, 200],
    }
    df = pd.DataFrame(sample_data)
    required_columns = ["product_id", "stock_level", "price"]
    if validate_dataframe(df, required_columns):
        log_message("DataFrame validation successful.")

    # Get current timestamp
    print(f"Current Timestamp: {get_current_timestamp()}")

    # Create a directory
    log_directory = "logs"
    create_directory(log_directory)
