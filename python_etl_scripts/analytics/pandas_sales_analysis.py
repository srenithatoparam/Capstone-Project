import pandas as pd
import os
import logging

# Configure logging for analytics execution
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# File paths
PROCESSED_DATA_PATH = "data/processed/superstore_cleaned.parquet"
ANALYTICS_OUTPUT_PATH = "data/processed/pandas_analytics"


def load_clean_data(file_path):
    """Load cleaned parquet data"""
    try:
        logging.info("Loading cleaned SuperStore data")
        return pd.read_parquet(file_path)
    except Exception as e:
        logging.error(f"Failed to load cleaned data: {e}")
        raise


def sales_profit_trend(df):
    """Sales and profit trend over time"""
    df["Order Month"] = df["Order Date"].dt.to_period("M").astype(str)

    trend = (
        df.groupby("Order Month")
        .agg(
            Total_Sales=("Sales", "sum"),
            Total_Profit=("Profit", "sum")
        )
        .reset_index()
        .sort_values("Order Month")
    )

    return trend


def category_performance(df):
    """Category and sub-category performance"""
    category_summary = (
        df.groupby(["Category", "Sub-Category"])
        .agg(
            Total_Sales=("Sales", "sum"),
            Total_Profit=("Profit", "sum")
        )
        .reset_index()
        .sort_values("Total_Sales", ascending=False)
    )

    return category_summary


def loss_making_products(df):
    """Identify loss-making products"""
    loss_products = (
        df.groupby("Product Name")
        .agg(Total_Profit=("Profit", "sum"))
        .reset_index()
    )

    loss_products = loss_products[loss_products["Total_Profit"] < 0] \
        .sort_values("Total_Profit")

    return loss_products


def regional_performance(df):
    """Regional sales and profit comparison"""
    region_summary = (
        df.groupby("Region")
        .agg(
            Total_Sales=("Sales", "sum"),
            Total_Profit=("Profit", "sum")
        )
        .reset_index()
        .sort_values("Total_Sales", ascending=False)
    )

    return region_summary


if __name__ == "__main__":

    try:
        # Load cleaned dataset
        df = load_clean_data(PROCESSED_DATA_PATH)

        # Create output directory if not exists
        os.makedirs(ANALYTICS_OUTPUT_PATH, exist_ok=True)

        # Generate analytics
        logging.info("Running Pandas analytics")

        trend_df = sales_profit_trend(df)
        category_df = category_performance(df)
        loss_df = loss_making_products(df)
        region_df = regional_performance(df)

        # Save analytics outputs
        trend_df.to_csv(
            f"{ANALYTICS_OUTPUT_PATH}/sales_profit_trend.csv",
            index=False
        )

        category_df.to_csv(
            f"{ANALYTICS_OUTPUT_PATH}/category_subcategory_performance.csv",
            index=False
        )

        loss_df.to_csv(
            f"{ANALYTICS_OUTPUT_PATH}/loss_making_products.csv",
            index=False
        )

        region_df.to_csv(
            f"{ANALYTICS_OUTPUT_PATH}/regional_performance.csv",
            index=False
        )

        logging.info("Pandas sales analytics completed successfully")

    except Exception as e:
        logging.critical(f"Pandas analytics pipeline failed: {e}")
