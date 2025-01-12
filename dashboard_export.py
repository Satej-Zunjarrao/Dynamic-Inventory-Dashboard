"""
Module: Dashboard Export
Author: Satej
Description: This module prepares and exports data for visualization in Power BI or Tableau dashboards.
"""

import pandas as pd

def export_to_dashboard_format(data, output_path):
    """
    Prepare and export data to a format suitable for Power BI or Tableau visualization.
    
    Args:
        data (pd.DataFrame): The processed DataFrame.
        output_path (str): Path to save the dashboard-ready data file.
    
    Returns:
        None
    """
    try:
        # Selecting relevant columns for the dashboard
        dashboard_data = data[[
            "product_id", 
            "product_category", 
            "stock_level", 
            "predicted_demand", 
            "last_updated"
        ]]

        # Save the prepared data to a CSV file
        dashboard_data.to_csv(output_path, index=False)
        print(f"Data exported successfully to {output_path} for dashboard visualization.")

    except Exception as e:
        print(f"Error exporting data for dashboard: {e}")
        raise

if __name__ == "__main__":
    # Example usage
    processed_data_path = "path/to/processed_data.csv"  # Replace with actual path
    dashboard_export_path = "path/to/dashboard_ready_data.csv"  # Replace with actual export path

    # Load processed data
    processed_data = pd.read_csv(processed_data_path)

    # Export to dashboard-ready format
    export_to_dashboard_format(processed_data, dashboard_export_path)
