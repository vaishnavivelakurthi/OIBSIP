# -------------------------------
# Essential Data Cleaning Template
# -------------------------------

import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("AB_NYC_2019.CSV")   # Replace with your file name

# -------------------------------
# 1. QUICK OVERVIEW
# -------------------------------
print("\n--- Data Overview ---")
print(df.head())
print(df.info())
print(df.describe(include='all'))

# -------------------------------
# 2. CHECK FOR MISSING VALUES
# -------------------------------
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Fill missing text fields with "Unknown"
text_columns = ['name', 'host_name', 'neighbourhood_group', 'neighbourhood', 'room_type']
for col in text_columns:
    df[col] = df[col].fillna("Unknown")

# Fill numeric missing with median
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Fill missing dates (last_review)
df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')
df['last_review'] = df['last_review'].fillna(df['last_review'].mode()[0])

# -------------------------------
# 3. HANDLE DUPLICATES
# -------------------------------
before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]

print(f"\nDuplicates Removed: {before - after}")

# -------------------------------
# 4. FIX DATA TYPES
# -------------------------------
df['id'] = df['id'].astype(int)
df['host_id'] = df['host_id'].astype(int)
df['price'] = df['price'].astype(float)
df['minimum_nights'] = df['minimum_nights'].astype(int)
df['availability_365'] = df['availability_365'].astype(int)

# -------------------------------
# 5. CLEAN TEXT COLUMNS (strip spaces, lower case)
# -------------------------------
for col in text_columns:
    df[col] = df[col].str.strip().str.title()

# -------------------------------
# 6. OUTLIER HANDLING
# -------------------------------

# Define outliers using IQR
def remove_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return df[(df[column] >= lower) & (df[column] <= upper)]

# Remove outliers for selected columns
for col in ['price', 'minimum_nights', 'availability_365']:
    df = remove_outliers_iqr(df, col)

# -------------------------------
# 7. STANDARDIZE / NORMALIZE (Optional)
# -------------------------------
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df[['price', 'minimum_nights', 'number_of_reviews']] = scaler.fit_transform(
    df[['price', 'minimum_nights', 'number_of_reviews']]
)

# -------------------------------
# 8. SAVE CLEANED DATASET
# -------------------------------
df.to_csv("airbnb_cleaned.csv", index=False)

print("\nData Cleaning Complete! Saved as airbnb_cleaned.csv")