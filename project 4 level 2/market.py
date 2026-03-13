import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 4 level 2\playstore_duplicates_removed.csv")
df.columns = df.columns.str.strip()

# Convert 'Installs' and 'Price' safely
df['Installs'] = df['Installs'].astype(str).str.replace(',', '').str.replace('+','')
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')
df['Price'] = df['Price'].astype(str).str.replace('$','')
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# Drop rows with missing critical values
df = df.dropna(subset=['Category', 'Installs', 'Price'])

# -----------------------------
# 1️⃣ Average Installs by Category
# -----------------------------
avg_installs = df.groupby('Category')['Installs'].mean().sort_values(ascending=False)

plt.figure(figsize=(12,6))
sns.barplot(x=avg_installs.index, y=avg_installs.values, palette="viridis")
plt.xticks(rotation=45, ha='right')
plt.title("Average Installs by App Category")
plt.ylabel("Average Installs")
plt.xlabel("Category")
plt.show()

# -----------------------------
# 2️⃣ Price vs Installs Scatter Plot
# -----------------------------
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='Price', y='Installs', alpha=0.5)
plt.title("Price vs Installs")
plt.xlabel("Price ($)")
plt.ylabel("Installs")
plt.ylim(0, 1e7)
plt.show()