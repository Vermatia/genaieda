"""Launch D-Tale for interactive EDA on the sales dataset.

This script loads the sales data, starts the D-Tale GUI in the browser,
and prints the local URL for the interactive dashboard.
"""

from __future__ import annotations

import sys
import time
import webbrowser
from pathlib import Path

import pandas as pd
import dtale


def load_sales_data(csv_path: str) -> pd.DataFrame:
    """Load the sales dataset into a pandas DataFrame with error handling."""
    print(f"Loading dataset from {csv_path}...")

    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {csv_path}")

    try:
        df = pd.read_csv(path)
        print(f"Dataset loaded successfully. Shape: {df.shape}")
        return df
    except Exception as exc:
        raise RuntimeError(f"Failed to read the dataset: {exc}") from exc


def launch_dtale(df: pd.DataFrame) -> None:
    """Launch the D-Tale GUI in the browser window and keep it alive."""
    print("Launching D-Tale...")
    d = dtale.show(df, host="127.0.0.1", port=40000)
    main_url = d.main_url()
    print("D-Tale started successfully.")
    print(f"Open this URL in your browser: {main_url}")

    try:
        webbrowser.open(main_url, new=2)
    except Exception as exc:
        print(f"Could not open browser automatically: {exc}")

    print("D-Tale is running. Press Ctrl+C in this terminal to stop it.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping D-Tale server...")
        try:
            d.kill()
        except Exception:
            pass
        print("D-Tale stopped.")


def main() -> int:
    """Run the workflow for loading and launching D-Tale."""
    try:
        df = load_sales_data("sales_data.csv")
        launch_dtale(df)
        print("Interactive EDA session ready.")
        return 0
    except Exception as exc:
        print(f"Error while starting D-Tale: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
