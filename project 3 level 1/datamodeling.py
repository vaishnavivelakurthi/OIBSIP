import pandas as pd
import numpy as np

# -----------------------------
# 1. Load dataset safely
# -----------------------------
file_path = r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 3 level 1\airbnb_cleaned.csv"   # replace with your dataset path
# file_path = r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 2 level 2\airbnb_cleaned.csv"  # replace with your dataset path
df = pd.read_csv(file_path)

# -----------------------------
# 2. Standardize column names
# -----------------------------
df.columns = (
    df.columns.str.strip()        # remove extra spaces
              .str.lower()        # lowercase
              .str.replace(" ", "_")
              .str.replace("-", "_")
)

# -----------------------------
# 3. Handle missing values
# -----------------------------
# Fill numeric missing values with median
num_cols = df.select_dtypes(include=["int64", "float64"]).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# Fill text missing data with "Unknown"
cat_cols = df.select_dtypes(include=["object"]).columns
df[cat_cols] = df[cat_cols].fillna("Unknown")

# -----------------------------
# 4. Remove duplicates
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# 5. Remove unrealistic values
# -----------------------------
df = df[df["price"] > 0]
df = df[df["minimum_nights"] <= 365]

# Optional: cap extreme values (outliers)
df["price"] = np.where(df["price"] > 1000, 1000, df["price"])

# -----------------------------
# 6. Feature Engineering
# -----------------------------
df["price_per_min_night"] = df["price"] / df["minimum_nights"]
df["review_rate"] = df["reviews_per_month"] / df["availability_365"]

# Handle division errors
df["review_rate"] = df["review_rate"].replace([np.inf, -np.inf], 0).fillna(0)

# -----------------------------
# 7. Save cleaned dataset for modeling
# -----------------------------
output_path ="airbnb_model_ready.csv"
df.to_csv(output_path, index=False)

print("🎉 Dataset cleaned and ready for modeling!")
print("Saved to:", output_path)