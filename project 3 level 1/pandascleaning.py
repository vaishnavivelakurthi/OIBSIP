# ---------------------------------------------------------
# IMPROVED PYTHON / PANDAS CLEANING WORKFLOW
# ---------------------------------------------------------

import pandas as pd
import numpy as np

# Load dataset (Update file name)
df = pd.read_csv("airbnb_cleaned.csv")

# ---------------------------------------------
# 1. Clean Column Names (snake_case)
# ---------------------------------------------
df.columns = (
    df.columns.str.strip()
              .str.lower()
              .str.replace(" ", "_")
              .str.replace("-", "_")
)

# ---------------------------------------------
# 2. Remove Duplicates
# ---------------------------------------------
df = df.drop_duplicates()

# ---------------------------------------------
# 3. Handle Missing Values
# ---------------------------------------------

# Convert dates
df["last_review"] = pd.to_datetime(df["last_review"], errors="coerce")

# Numeric columns → fill with median
num_cols = df.select_dtypes(include=["int64", "float64"]).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# Categorical columns → fill with string placeholder
cat_cols = df.select_dtypes(include=["object"]).columns
df[cat_cols] = df[cat_cols].fillna("Unknown")

# ---------------------------------------------
# 4. Fix Data Types
# ---------------------------------------------
df["id"] = df["id"].astype(int)
df["host_id"] = df["host_id"].astype(int)
df["price"] = df["price"].astype(float)
df["minimum_nights"] = df["minimum_nights"].astype(int)
df["availability_365"] = df["availability_365"].astype(int)

# ---------------------------------------------
# 5. Clean Text Columns (formatting)
# ---------------------------------------------
for col in ["name", "host_name", "neighbourhood", "neighbourhood_group", "room_type"]:
    df[col] = df[col].astype(str).str.strip().str.title()

# ---------------------------------------------
# 6. Outlier Treatment (IQR)
# ---------------------------------------------
def cap_outliers(df, col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df[col] = df[col].clip(lower, upper)
    return df

for col in ["price", "minimum_nights", "availability_365", "number_of_reviews"]:
    df = cap_outliers(df, col)

# ---------------------------------------------
# Save cleaned dataset
# ---------------------------------------------
df.to_csv("airbnb_clean_for_analysis.csv", index=False)

print("Cleaned dataset saved as airbnb_clean_for_analysis.csv")