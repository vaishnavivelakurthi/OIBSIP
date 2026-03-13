# File: remove_duplicate_apps.py

import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 4 level 2\user_reviews.csv")
print("Original Dataset Shape:", df.shape)

# Check duplicate apps
duplicate_apps = df[df.duplicated(subset='App', keep=False)]

print("\nSample Duplicate Apps:")
print(duplicate_apps[['App','Category','Rating','Reviews']].head())

# Count duplicates
duplicate_count = df.duplicated(subset='App').sum()
print("\nTotal Duplicate Apps:", duplicate_count)

# Remove duplicates (keep the first occurrence)
df_clean = df.drop_duplicates(subset='App', keep='first')

print("\nDataset Shape After Removing Duplicates:", df_clean.shape)

# Save cleaned dataset
df_clean.to_csv("playstore_duplicates_removed.csv", index=False)

print("\nCleaned dataset saved as: playstore_duplicates_removed.csv")