# File: category_distribution_analysis.py

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 4 level 2\apps.csv")

# Count number of apps in each category
category_counts = df['Category'].value_counts()

print("Number of Apps in Each Category:\n")
print(category_counts)

# Convert to dataframe for better display
category_df = category_counts.reset_index()
category_df.columns = ['Category', 'App_Count']

# Save results
category_df.to_csv("category_distribution.csv", index=False)

print("\nCategory distribution saved as: category_distribution.csv")

# Plot bar chart
plt.figure(figsize=(12,6))
category_counts.plot(kind='bar')

plt.title("Distribution of Apps Across Categories")
plt.xlabel("Category")
plt.ylabel("Number of Apps")
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()