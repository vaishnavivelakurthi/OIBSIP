# Import libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Load dataset
df = pd.read_csv(r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 2 level 2\WineQT.csv") # Replace with your file path

# Display original feature ranges
print("Original Feature Ranges:")
print(df[['fixed acidity', 'alcohol']].describe())

# 1. Standardization (mean=0, std=1)
scaler = StandardScaler()
df_scaled = df.copy()
df_scaled[['fixed acidity', 'alcohol']] = scaler.fit_transform(df_scaled[['fixed acidity', 'alcohol']])
print("\nAfter Standardization:")
print(df_scaled[['fixed acidity', 'alcohol']].describe())

# 2. Min-Max Normalization (0-1)
minmax_scaler = MinMaxScaler()
df_normalized = df.copy()
df_normalized[['fixed acidity', 'alcohol']] = minmax_scaler.fit_transform(df_normalized[['fixed acidity', 'alcohol']])
print("\nAfter Min-Max Normalization:")
print(df_normalized[['fixed acidity', 'alcohol']].describe())