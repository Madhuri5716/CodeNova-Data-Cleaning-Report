# Task 2 — Data Cleaning Report

## Objective
Audit a customer dataset, correct inconsistent values, document cleaning decisions, and compare data quality before and after processing.

## Dataset
`data/raw_customers.csv` is synthetic demonstration data with intentional missing values, a duplicate, inconsistent city capitalization, an invalid date, and invalid age values. It is not real customer data.

## Tools
Python 3, pandas, NumPy.

## Run
Install dependencies with `pip install pandas numpy`, then run `python clean_data.py`.

## Outputs
- `outputs/clean_customers.csv`
- `outputs/before_after_profile.csv`
- `outputs/data_quality_report.md`

## Cleaning decisions
The script standardizes city names, converts columns to suitable types, removes exact duplicate rows, treats out-of-range ages as missing, fills missing numeric values with medians, labels missing cities as `Unknown`, and flags spending outliers using IQR. The original raw file is never overwritten.

## Limitations
The age range is a demonstration assumption. Imputation strategies should be selected based on the dataset's meaning and context.
