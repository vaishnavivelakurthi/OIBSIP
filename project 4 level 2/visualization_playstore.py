import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv(r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 4 level 2\playstore_no_outliers.csv")

# Strip column names just in case
df.columns = df.columns.str.strip()

# Display first few rows
print(df.head())

# -----------------------------
# 1️⃣ Category Distribution (Bar Plot)
# -----------------------------
plt.figure(figsize=(12,6))
category_counts = df['Category'].value_counts()
sns.barplot(x=category_counts.index, y=category_counts.values, palette="viridis")
plt.xticks(rotation=90)
plt.title("Number of Apps per Category")
plt.xlabel("Category")
plt.ylabel("Number of Apps")
plt.tight_layout()
plt.show()

# -----------------------------
# 2️⃣ Scatter Plot: Rating vs. Reviews (Large datasets)
# -----------------------------
plt.figure(figsize=(10,6))
# Use alpha to handle overlapping points
sns.scatterplot(x='Reviews', y='Rating', data=df, alpha=0.5)
plt.title("App Rating vs. Number of Reviews")
plt.xlabel("Number of Reviews")
plt.ylabel("Rating")
plt.ylim(0,5)
plt.xscale('log')  # Reviews often have wide range; log scale helps
plt.show()

# -----------------------------
# 3️⃣ Box Plot: Price distribution per Type (Free vs Paid)
# -----------------------------
plt.figure(figsize=(8,5))
sns.boxplot(x='Type', y='Price', data=df, palette="Set2")
plt.title("Price Distribution by App Type")
plt.ylim(0, 50)  # Limit y-axis to remove extreme prices
plt.show()

# -----------------------------
# 4️⃣ Correlation Heatmap (Numeric Features)
# -----------------------------
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
plt.figure(figsize=(10,8))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap of Numeric Features")
plt.show()