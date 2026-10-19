# Data Quality Audit Report

## Objective
Identify missing values, duplicates, inconsistent city names, invalid values and potential spending outliers.

## Input protection
The original `data/raw_customers.csv` is not overwritten. The cleaned file is saved separately.

## Cleaning steps
1. Standardized city names using trimming and title case.
2. Converted numeric columns and signup dates to suitable types.
3. Removed exact duplicate rows.
4. Marked ages outside 0–100 as missing (a demonstration assumption).
5. Imputed missing numeric values with the column median.
6. Replaced missing city values with `Unknown`.
7. Used the IQR method to flag spending outliers instead of deleting them automatically.

## Outputs
- `outputs/clean_customers.csv`
- `outputs/before_after_profile.csv`
- `outputs/data_quality_report.md`

## Limitations
Median imputation is a simple baseline. A real project should investigate why values are missing and validate age rules with domain knowledge. Potential outliers may be valid observations and require review.
