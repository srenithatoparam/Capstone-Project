import pandas as pd
import os
import logging

# Configure logging for monitoring pipeline execution
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Path to raw SuperStore CSV file
RAW_DATA_PATH = "data/raw/Sample - Superstore.csv"

# Expected dataset schema for validation
EXPECTED_COLUMNS = [
    "Order ID", "Order Date", "Ship Date", "Ship Mode",
    "Customer ID", "Customer Name", "Segment",
    "Country", "City", "State", "Postal Code", "Region",
    "Product ID", "Category", "Sub-Category", "Product Name",
    "Sales", "Quantity", "Discount", "Profit"
]

# Columns that should contain date values
DATE_COLUMNS = ["Order Date", "Ship Date"]

# Columns that should contain numeric values
NUMERIC_COLUMNS = ["Sales", "Quantity", "Discount", "Profit"]


def read_raw_data(file_path):
    """Read raw SuperStore CSV file"""
    try:
        logging.info("Reading raw SuperStore data")
        df = pd.read_csv(file_path, encoding="latin1")  # Load CSV file
        logging.info("Raw data loaded successfully")
        return df
    except FileNotFoundError:
        logging.error("Raw data file not found")
        raise
    except Exception as e:
        logging.error(f"Error while reading raw data: {e}")
        raise


def validate_schema(df):
    """Check whether all expected columns are present"""
    missing_cols = set(EXPECTED_COLUMNS) - set(df.columns)
    if missing_cols:
        logging.error(f"Schema validation failed. Missing columns: {missing_cols}")
        raise ValueError("Schema validation failed")
    logging.info("Schema validation passed")


def validate_date_columns(df):
    """Convert date columns and identify invalid values"""
    for col in DATE_COLUMNS:
        df[col] = pd.to_datetime(df[col], errors="coerce")  # Convert to datetime

    invalid_dates = df[DATE_COLUMNS].isnull().sum()  # Count invalid dates
    logging.info(f"Invalid date values count:\n{invalid_dates}")


def validate_numeric_columns(df):
    """Convert numeric columns and identify invalid values"""
    for col in NUMERIC_COLUMNS:
        df[col] = pd.to_numeric(df[col], errors="coerce")  # Convert to numeric

    invalid_numbers = df[NUMERIC_COLUMNS].isnull().sum()  # Count invalid numbers
    logging.info(f"Invalid numeric values count:\n{invalid_numbers}")


if __name__ == "__main__":

    try:
        # Load raw dataset
        df_raw = read_raw_data(RAW_DATA_PATH)

        # Log dataset basic information
        logging.info(f"Dataset Shape: {df_raw.shape}")
        logging.info(f"Column Names: {df_raw.columns.tolist()}")
        logging.info(f"Missing Values Count:\n{df_raw.isnull().sum()}")

        # Perform schema, date, and numeric validations
        validate_schema(df_raw)
        validate_date_columns(df_raw)
        validate_numeric_columns(df_raw)

        logging.info("Data ingestion validation completed successfully")

        # Display sample records for verification
        logging.info(f"Data Preview:\n{df_raw.head()}")

    except Exception as e:
        logging.critical(f"Ingestion pipeline failed: {e}")
