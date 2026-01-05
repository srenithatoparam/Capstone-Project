import pandas as pd
import os
import logging

# Configure logging for pipeline monitoring
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# File paths
RAW_DATA_PATH = "data/raw/Sample - Superstore.csv"
PROCESSED_DATA_PATH = "data/processed/superstore_cleaned.parquet"
PANDAS_SUMMARY_PATH = "data/processed/pandas_sales_summary.csv"


def load_raw_data(file_path):
    """Load raw CSV file"""
    try:
        logging.info("Loading raw CSV data")
        return pd.read_csv(file_path, encoding="latin1")  # Read CSV file
    except Exception as e:
        logging.error(f"Failed to load raw data: {e}")
        raise


def clean_data(df):
    """Clean and transform raw dataset"""
    try:
        logging.info("Starting data cleaning process")

        # Convert date columns to datetime format
        df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
        df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Handle missing numeric values
        df["Postal Code"] = df["Postal Code"].fillna(0)
        df["Sales"] = df["Sales"].fillna(0)
        df["Profit"] = df["Profit"].fillna(0)

        # Standardize categorical text columns
        df["Region"] = df["Region"].str.title().str.strip()
        df["Category"] = df["Category"].str.title().str.strip()
        df["Sub-Category"] = df["Sub-Category"].str.title().str.strip()

        # Create derived metric: Profit Margin
        df["Profit Margin"] = df["Profit"] / df["Sales"]
        df["Profit Margin"] = df["Profit Margin"].replace(
            [float("inf"), -float("inf")], 0
        ).fillna(0)

        logging.info("Data cleaning completed successfully")
        return df

    except Exception as e:
        logging.error(f"Error during data cleaning: {e}")
        raise


def pandas_sales_summary(df):
    """Create category-level sales summary using Pandas"""
    try:
        logging.info("Generating Pandas sales summary")

        # Filter records with valid sales
        df_filtered = df[df["Sales"] > 0]

        # Group and aggregate sales data
        summary = (
            df_filtered
            .groupby("Category")
            .agg(
                Total_Sales=("Sales", "sum"),
                Total_Profit=("Profit", "sum"),
                Avg_Profit_Margin=("Profit Margin", "mean")
            )
            .reset_index()
        )

        logging.info("Pandas aggregation completed successfully")
        return summary

    except Exception as e:
        logging.error(f"Error during Pandas aggregation: {e}")
        raise


if __name__ == "__main__":

    try:
        # Load raw dataset
        df_raw = load_raw_data(RAW_DATA_PATH)

        # Clean and transform data
        df_cleaned = clean_data(df_raw)

        # Generate Pandas aggregation summary
        pandas_summary = pandas_sales_summary(df_cleaned)

        # Create processed folder if not exists
        os.makedirs("data/processed", exist_ok=True)

        # Save cleaned dataset in parquet format
        df_cleaned.to_parquet(PROCESSED_DATA_PATH, index=False)

        # Save Pandas aggregation output
        pandas_summary.to_csv(PANDAS_SUMMARY_PATH, index=False)

        logging.info("Data cleaning and transformation pipeline executed successfully")

    except Exception as e:
        logging.critical(f"Pipeline execution failed: {e}")
