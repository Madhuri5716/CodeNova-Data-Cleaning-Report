from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)
df = pd.read_csv(ROOT / "data" / "raw_customers.csv")
before = {"Stage":"Before cleaning","Rows":len(df),"Columns":len(df.columns),
          "Missing_Cells":int(df.isna().sum().sum()),"Duplicate_Rows":int(df.duplicated().sum())}

df["City"] = df["City"].astype("string").str.strip().str.title()
for col in ["Age","Orders","Spend_INR"]:
    df[col] = pd.to_numeric(df[col],errors="coerce")
df["Signup_Date"] = pd.to_datetime(df["Signup_Date"],errors="coerce")
df = df.drop_duplicates()
df.loc[~df["Age"].between(0,100),"Age"] = np.nan
for col in ["Age","Orders","Spend_INR"]:
    df[col] = df[col].fillna(df[col].median())
df["City"] = df["City"].fillna("Unknown")
q1, q3 = df["Spend_INR"].quantile([.25,.75])
iqr = q3-q1
lower, upper = q1-1.5*iqr, q3+1.5*iqr
df["Spend_Outlier_Flag"] = ~df["Spend_INR"].between(lower,upper)
after = {"Stage":"After cleaning","Rows":len(df),"Columns":len(df.columns),
         "Missing_Cells":int(df.isna().sum().sum()),"Duplicate_Rows":int(df.duplicated().sum())}
pd.DataFrame([before,after]).to_csv(OUT/"before_after_profile.csv",index=False)
df.to_csv(OUT/"clean_customers.csv",index=False)
report = '''# Data Quality Audit Report

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
'''
(OUT/"data_quality_report.md").write_text(report)
print("Data cleaning completed. Outputs saved in:", OUT)
print(pd.DataFrame([before,after]).to_string(index=False))
