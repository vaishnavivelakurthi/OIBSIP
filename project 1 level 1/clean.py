import pandas as pd
import numpy as np

# -----------------------------
# 1. Load the Dataset
# -----------------------------
df = pd.read_csv("retail_sales_dataset.csv")

# Show first 5 rows
print(df.head())

# -----------------------------
# 2. Check Basic Info
# -----------------------------
print(df.info())
print(df.describe(include="all"))

# -----------------------------
# 3. Handling Missing Values
# -----------------------------

# Check missing values
print(df.isnull().sum())

# Fill or remove missing values
df['Gender'] = df['Gender'].fillna("Unknown")
df['Age'] = df['Age'].fillna(df['Age'].median())  # Replace with median age
df['Product Category'] = df['Product Category'].fillna("Not Specified")

# Drop rows where essential fields are missing
df = df.dropna(subset=['Transaction ID', 'Customer ID', 'Quantity', 'Price per Unit'])

# -----------------------------
# 4. Convert Data Types
# -----------------------------

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Convert numeric columns
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Price per Unit'] = pd.to_numeric(df['Price per Unit'], errors='coerce')

# -----------------------------
# 5. Fix Incorrect or Dirty Data
# -----------------------------

# Remove negative or zero quantities
df = df[df['Quantity'] > 0]

# Remove negative prices
df = df[df['Price per Unit'] > 0]

# Standardize Gender values
df['Gender'] = df['Gender'].str.capitalize()   # male → Male, FEMALE → Female

# Remove duplicates
df = df.drop_duplicates()

# -----------------------------
# 6. Create or Correct Total Amount Column
# -----------------------------
df['Total Amount'] = df['Quantity'] * df['Price per Unit']

# -----------------------------
# 7. Reset Index (after cleaning)
# -----------------------------
df = df.reset_index(drop=True)

# -----------------------------
# 8. Save Cleaned Dataset
# -----------------------------
df.to_csv("retail_sales_cleaned.csv", index=False)

print("Data Cleaning Completed Successfully!")
print(df.head())