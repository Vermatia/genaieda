# GenAI-Powered Automated EDA Pipeline 🚀

An end-to-end Exploratory Data Analysis (EDA) project that programmatically generates a large-scale dataset and performs deep automated data profiling. This project demonstrates how to simulate real-world data pipelines and leverage modern profiling libraries to uncover data quality insights efficiently.

---

## 📋 Table of Contents
* [About the Project](#about-the-project)
* [Project Workflow](#project-workflow)
* [Tools & Technologies Used](#tools--technologies-used)
* [How to Run the Project](#how-to-run-the-project)
* [EDA Highlights](#eda-highlights)

---

## 🔍 About the Project
In real-world data science workflows, analysts often need to inspect large volumes of data quickly. This project simulates that environment by:
1. Programmatically generating a custom synthetic sales dataset containing **1,000,000 rows** using a Python script.
2. Automating the Exploratory Data Analysis (EDA) process using advanced profiling tools to inspect distributions, missing values, correlations, and feature characteristics.

---

## 🛠️ Tools & Technologies Used
* **Python**: Core scripting and logic.
* **Pandas / NumPy**: Large-scale data manipulation and handling.
* **YData-Profiling**: Comprehensive statistical reports and data health checks.
* **Sweetviz**: Fast, visual exploratory data analysis and target comparison reports.
* **Git & GitHub**: Version control and portfolio presentation.

---

## ⚙️ Project Workflow
```text
├── create_sales_dataset.py   # Python script to generate the 1M-row sales dataset
├── sales_data.csv            # (Ignored in Git) Generated locally when script runs
├── eda_analysis.ipynb        # Jupyter notebook executing ydata-profiling & Sweetviz
├── .gitignore                # Excludes data files, virtual environments, and caches
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation


---

## 🚀 How to Run the Project

Get this project up and running on your local machine in just a few simple steps:

> [!TIP]
> **Prerequisite:** Make sure you have Python installed on your system before proceeding.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name

   ---

## 🛠️ Step-by-Step Execution Guide

### Step 1: Install Required Dependencies
Before running the project scripts, ensure you have all necessary Python libraries installed. 

> [!TIP]
> It is recommended to run this inside a clean virtual environment.

Run the following command in your terminal to install everything specified in the requirements file:
```bash
pip install -r requirements.txt


Step 2: Generate the Synthetic Dataset
To simulate a real-world analytics pipeline, you will first generate a large-scale local dataset.

Locate the generation script in your root folder: create_sales_dataset.py

Execute the script via your terminal:

Bash
python create_sales_dataset.py
[!NOTE]
What this does: This script programmatically builds a clean, highly structured sales dataset containing 1,000,000 rows ⚡ (Kept local and excluded from Git via .gitignore to save space and protect data


Step 3: Execute the Automated EDA
With your dataset generated locally, you can now run the automated profiling pipelines.

