# File: handle_missing_values.py

import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 4 level 2\apps.csv")

print("Dataset Shape:", df.shape)

# Check missing values
print("\nMissing Values Before Handling:")
print(df['Rating'].isnull().sum())


# Display rows where Rating is missing
missing_ratings = df[df['Rating'].isnull()]
print("\nApps with Missing Ratings:")
print(missing_ratings[['App','Rating']].head())


# Fill missing ratings using mean rating
mean_rating = df['Rating'].mean()
df['Rating'].fillna(mean_rating, inplace=True)


# Check again
print("\nMissing Values After Handling:")
print(df['Rating'].isnull().sum())


# Save updated dataset
df.to_csv("playstore_missing_values_fixed.csv", index=False)

print("\nCleaned dataset saved as: playstore_missing_values_fixed.csv")