import pandas as pd
import numpy as np

# ----------------------------------------------------------
# 1. LOAD RAW DATA
# ----------------------------------------------------------
df = pd.read_csv("airbnb_cleaned.csv")   # Replace with your dataset filename
print("Raw data shape:", df.shape)


# ----------------------------------------------------------
# 2. VALIDATE STRUCTURE (Ensure all expected columns exist)
# ----------------------------------------------------------
expected_columns = [
    "id","name","host_id","host_name","neighbourhood_group","neighbourhood",
    "latitude","longitude","room_type","price","minimum_nights",
    "number_of_reviews","last_review","reviews_per_month",
    "calculated_host_listings_count","availability_365"
]

# Fix column order if not matching
df = df[[col for col in expected_columns if col in df.columns]]
print("\nColumns after reordering/validation:")
print(df.columns)


# ----------------------------------------------------------
# 3. HANDLE MISSING VALUES
# ----------------------------------------------------------

# Convert last_review to datetime
df["last_review"] = pd.to_datetime(df["last_review"], errors="coerce")

# Missing numeric values → median
numeric_cols = [
    "price","minimum_nights","number_of_reviews","reviews_per_month",
    "calculated_host_listings_count","availability_365"
]
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Missing categorical values → "Unknown"
text_cols = ["name","host_name","neighbourhood_group","neighbourhood","room_type"]
for col in text_cols:
    df[col] = df[col].fillna("Unknown")

# Missing dates → median date
df["last_review"] = df["last_review"].fillna(df["last_review"].median())


# ----------------------------------------------------------
# 4. REMOVE DUPLICATES
# ----------------------------------------------------------
before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]
print("\nDuplicates removed:", before - after)


# ----------------------------------------------------------
# 5. FIX DATA TYPES
# ----------------------------------------------------------
df["id"] = df["id"].astype(int)
df["host_id"] = df["host_id"].astype(int)
df["price"] = df["price"].astype(float)
df["minimum_nights"] = df["minimum_nights"].astype(int)
df["availability_365"] = df["availability_365"].astype(int)


# ----------------------------------------------------------
# 6. CLEAN TEXT COLUMNS
# ----------------------------------------------------------
for col in text_cols:
    df[col] = df[col].astype(str).str.strip().str.title()


# ----------------------------------------------------------
# 7. OUTLIER TREATMENT (IQR Method)
# ----------------------------------------------------------
def treat_outliers(df, col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR
    df[col] = np.where(df[col] < lower, lower, df[col])
    df[col] = np.where(df[col] > upper, upper, df[col])
    return df

for col in ["price", "minimum_nights", "availability_365", "number_of_reviews"]:
    df = treat_outliers(df, col)


# ----------------------------------------------------------
# 8. FEATURE ENGINEERING (Useful for analytics)
# ----------------------------------------------------------

# Days since last review
df["days_since_last_review"] = (pd.Timestamp.today() - df["last_review"]).dt.days
df["days_since_last_review"] = df["days_since_last_review"].fillna(
    df["days_since_last_review"].median()
)

# Review frequency normalization
df["reviews_per_year"] = df["number_of_reviews"] / (
    df["days_since_last_review"] / 365
)

# Active / inactive listing
df["is_active"] = df["availability_365"].apply(lambda x: 1 if x > 0 else 0)


# ----------------------------------------------------------
# 9. FINAL QUALITY CHECK
# ----------------------------------------------------------
print("\nFinal dataset info:")
print(df.info())

print("\nSummary statistics:")
print(df.describe())


# ----------------------------------------------------------
# 10. SAVE CLEANED DATASET
# ----------------------------------------------------------
df.to_csv("airbnb_cleaned_analytics_ready.csv", index=False)
print("\nSaved cleaned dataset as: airbnb_cleaned_analytics_ready.csv")