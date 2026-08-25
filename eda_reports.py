"""Generate automated EDA reports for the sales dataset.

This script verifies required library versions, loads the CSV file, creates
YData Profiling and Sweetviz reports, and saves them as HTML files.
"""

from __future__ import annotations

import os
import sys
import webbrowser
from importlib import metadata
from pathlib import Path

from packaging.version import Version

import pandas as pd


REQUIRED_PACKAGES = {
    "pandas": "2.0.0",
    "ydata-profiling": "4.6.0",
    "sweetviz": "2.3.0",
}


def check_package_versions() -> None:
    """Verify required package versions before running the EDA workflow."""
    print("Checking package versions...")

    for package_name, minimum_version in REQUIRED_PACKAGES.items():
        try:
            installed_version = metadata.version(package_name)
            print(f"{package_name}: {installed_version}")

            if Version(installed_version) < Version(minimum_version):
                raise RuntimeError(
                    f"{package_name} {installed_version} is installed, but version "
                    f"{minimum_version} or higher is required."
                )
        except metadata.PackageNotFoundError:
            raise RuntimeError(
                f"{package_name} is not installed. Please install it with: "
                f"python -m pip install \"{package_name}>={minimum_version}\""
            ) from None

    print("All required package versions are compatible.")


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


def open_report_in_browser(report_path: str) -> None:
    """Open a generated HTML report in the default browser."""
    absolute_path = os.path.abspath(report_path)
    normalized_path = absolute_path.replace("\\", "/")
    file_url = f"file:///{normalized_path}"
    webbrowser.open(file_url, new=2)
    print(f"Opened report in browser: {report_path}")


def create_ydata_report(df: pd.DataFrame, output_path: str = "ydata_report.html") -> None:
    """Generate a YData Profiling report with minimal mode for speed."""
    from ydata_profiling import ProfileReport

    print("Generating YData Profiling report...")
    report = ProfileReport(df, minimal=True)
    report.to_file(output_path)
    open_report_in_browser(output_path)
    print(f"YData report saved successfully as {output_path}")


def create_sweetviz_report(df: pd.DataFrame, output_path: str = "sweetviz_report.html") -> None:
    """Generate a Sweetviz report with revenue as the target variable."""
    import sweetviz as sv

    print("Generating Sweetviz report...")
    df_for_report = df.copy()
    df_for_report["revenue"] = df_for_report["revenue"].fillna(0.0)
    report = sv.analyze(df_for_report, target_feat="revenue")
    report.show_html(output_path)
    open_report_in_browser(output_path)
    print(f"Sweetviz report saved successfully as {output_path}")


def main() -> int:
    """Execute the full EDA automation workflow."""
    try:
        check_package_versions()
        df = load_sales_data("sales_data.csv")
        create_ydata_report(df)
        create_sweetviz_report(df)
        print("EDA workflow completed successfully.")
        return 0
    except Exception as exc:
        print(f"Error during EDA workflow: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
