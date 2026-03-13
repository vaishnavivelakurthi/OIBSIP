

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df =pd.read_csv(r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 2 level 2\WineQT.csv")

print("=== Dataset Head ===")
print(df.head())

# 1. Check for missing values
print("\n=== Missing Values ===")
missing = df.isnull().sum()
print(missing)

# Save missing value info
missing.to_csv("missing_values_output.csv")

# Handle missing values (fill numeric with mean)
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

print("\n=== Missing Values After Imputation ===")
print(df.isnull().sum())

# 2. Check for inconsistent data types
print("\n=== Data Types ===")
print(df.dtypes)

# Convert any object columns with numeric strings to float
for col in df.columns:
    if df[col].dtype == 'object':
        try:
            df[col] = df[col].astype(float)
        except:
            pass

print("\n=== Data Types After Conversion ===")
print(df.dtypes)

# Save data types
df.dtypes.to_csv("data_types_output.csv")

# 3. Detect outliers using IQR
print("\n=== Outlier Detection ===")
outlier_summary = {}
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    outlier_summary[col] = len(outliers)
    print(f"{col}: {len(outliers)} outliers")
    
    # Boxplot for visualizing outliers
    plt.figure(figsize=(6,4))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.savefig(f"boxplot_{col}.png")
    plt.close()

# Save outlier summary
outlier_df = pd.DataFrame(list(outlier_summary.items()), columns=['Feature','Outliers'])
outlier_df.to_csv("outlier_summary.csv", index=False)

# 4. Save cleaned numeric dataset
df.to_csv("WineQT_numeric.csv", index=False)
print("\n=== Cleaned Dataset Saved as 'WineQT_numeric.csv' ===")
