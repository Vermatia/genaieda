"""Generate a sample sales dataset for Python EDA practice.

This script creates 100,000 rows of transaction data with realistic columns,
missing values, and a date range spanning 2023 to 2024.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd


def generate_sales_data(output_path: str = "sales_data.csv") -> pd.DataFrame:
    """Create the sample dataset and save it to CSV."""
    rng = np.random.default_rng(42)
    rows = 100_000

    # Basic transaction details
    transaction_ids = np.arange(1, rows + 1)
    customer_ids = rng.integers(1000, 100000, size=rows)

    products = [
        "Laptop",
        "Phone",
        "Tablet",
        "Headphones",
        "Monitor",
        "Keyboard",
        "Mouse",
        "Printer",
        "Camera",
        "Speaker",
    ]
    categories = [
        "Electronics",
        "Electronics",
        "Electronics",
        "Accessories",
        "Electronics",
        "Accessories",
        "Accessories",
        "Office",
        "Electronics",
        "Audio",
    ]
    product_to_category = dict(zip(products, categories))

    product_names = rng.choice(products, size=rows)
    category_names = [product_to_category[p] for p in product_names]
    quantities = rng.integers(1, 10, size=rows)

    # Prices with 5% missing values
    prices = np.round(rng.uniform(10.0, 499.99, size=rows), 2)
    missing_price_mask = rng.random(rows) < 0.05
    prices[missing_price_mask] = np.nan

    # Revenue is quantity * price. If a price is missing, set revenue to 0
    # so the dataset remains valid for downstream analysis and reporting.
    revenue = np.round(quantities * prices, 2)
    revenue[missing_price_mask] = 0.0

    # Date range from 2023 to 2024
    start_date = pd.Timestamp("2023-01-01")
    end_date = pd.Timestamp("2024-12-31")
    days_between = (end_date - start_date).days + 1
    date_offsets = rng.integers(0, days_between, size=rows)
    transaction_dates = start_date + pd.to_timedelta(date_offsets, unit="D")

    # Regions with 2% missing values
    regions = np.array(rng.choice(["North", "South", "East", "West", "Central"], size=rows), dtype=object)
    missing_region_mask = rng.random(rows) < 0.02
    regions[missing_region_mask] = np.nan

    df = pd.DataFrame(
        {
            "transaction_id": transaction_ids,
            "customer_id": customer_ids,
            "product": product_names,
            "category": category_names,
            "quantity": quantities,
            "price": prices,
            "revenue": revenue,
            "date": transaction_dates,
            "region": regions,
        }
    )

    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False)

    return df


def main() -> int:
    """Entry point with basic error handling and user-friendly output."""
    try:
        print("Starting dataset generation...")
        df = generate_sales_data("sales_data.csv")

        missing_price_pct = df["price"].isna().mean() * 100
        missing_region_pct = df["region"].isna().mean() * 100

        print("Dataset created successfully.")
        print(f"Rows generated: {len(df):,}")
        print(f"Columns: {list(df.columns)}")
        print(f"Missing price values: {missing_price_pct:.2f}%")
        print(f"Missing region values: {missing_region_pct:.2f}%")
        print("File saved as: sales_data.csv")
        return 0

    except Exception as exc:  # pragma: no cover - defensive programming
        print(f"Error generating dataset: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
