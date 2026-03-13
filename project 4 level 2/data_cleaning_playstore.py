# data_cleaning_playstore.py

import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 4 level 2\apps.csv")

print("Original Data")
print(df[['Installs','Price','Size']].head())


# -------- CLEAN INSTALLS COLUMN --------
df['Installs'] = df['Installs'].astype(str)
df['Installs'] = df['Installs'].str.replace('+','', regex=False)
df['Installs'] = df['Installs'].str.replace(',','', regex=False)

df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')


# -------- CLEAN PRICE COLUMN --------
df['Price'] = df['Price'].astype(str)
df['Price'] = df['Price'].str.replace('$','', regex=False)

df['Price'] = pd.to_numeric(df['Price'], errors='coerce')


# -------- CLEAN SIZE COLUMN --------
df['Size'] = df['Size'].astype(str)

# Remove unwanted text
df['Size'] = df['Size'].str.replace('Varies with device','')
df['Size'] = df['Size'].str.replace('M','')
df['Size'] = df['Size'].str.replace('k','')

# Convert to numeric
df['Size'] = pd.to_numeric(df['Size'], errors='coerce')


print("\nCleaned Data")
print(df[['Installs','Price','Size']].head())


# Save cleaned file
df.to_csv("cleaned_playstore_data.csv", index=False)

print("\nCleaned dataset saved as cleaned_playstore_data.csv")