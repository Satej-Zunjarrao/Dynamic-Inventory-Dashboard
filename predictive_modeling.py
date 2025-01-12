"""
Module: Predictive Modeling
Author: Satej
Description: This module implements predictive modeling to forecast inventory requirements 
using historical sales data and trends.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def prepare_features(data, target_column, feature_columns):
    """
    Prepare features and target variables for modeling.
    
    Args:
        data (pd.DataFrame): The input DataFrame.
        target_column (str): The column to be predicted.
        feature_columns (list): List of columns to be used as features.
    
    Returns:
        pd.DataFrame, pd.Series: Feature matrix (X) and target variable (y).
    """
    try:
        X = data[feature_columns]
        y = data[target_column]
        print("Features and target variables prepared.")
        return X, y
    except Exception as e:
        print(f"Error preparing features: {e}")
        raise

def train_model(X, y):
    """
    Train a Random Forest Regressor to predict inventory requirements.
    
    Args:
        X (pd.DataFrame): The feature matrix.
        y (pd.Series): The target variable.
    
    Returns:
        RandomForestRegressor: Trained model.
    """
    try:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestRegressor(random_state=42, n_estimators=100)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f"Model trained successfully. Mean Squared Error: {mse}")
        return model
    except Exception as e:
        print(f"Error training model: {e}")
        raise

def predict_inventory(model, new_data):
    """
    Predict inventory requirements using the trained model.
    
    Args:
        model (RandomForestRegressor): The trained model.
        new_data (pd.DataFrame): New data for prediction.
    
    Returns:
        np.ndarray: Predicted inventory requirements.
    """
    try:
        predictions = model.predict(new_data)
        print("Predictions generated successfully.")
        return predictions
    except Exception as e:
        print(f"Error generating predictions: {e}")
        raise

if __name__ == "__main__":
    # Example usage
    file_path = "path/to/inventory_data.csv"  # Replace with the actual path
    data = pd.read_csv(file_path)

    # Prepare features and target
    features = ["stock_level", "sales", "reorder_point"]  # Example feature columns
    target = "future_demand"  # Example target column
    X, y = prepare_features(data, target_column=target, feature_columns=features)

    # Train the predictive model
    model = train_model(X, y)

    # Predict on new data
    new_data = pd.DataFrame({
        "stock_level": [50, 20],
        "sales": [30, 15],
        "reorder_point": [10, 5]
    })
    predictions = predict_inventory(model, new_data)
    print("Predicted Inventory Requirements:", predictions)
