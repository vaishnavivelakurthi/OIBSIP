import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv(r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 4 level 2\playstore_no_outliers.csv")

# Strip column names to avoid accidental spaces
df.columns = df.columns.str.strip()

# Display first few rows
print(df.head())

# -----------------------------
# 1️⃣ Rating vs Installs
# -----------------------------
plt.figure(figsize=(10,6))
sns.scatterplot(x='Installs', y='Rating', data=df, alpha=0.5)
plt.xscale('log')  # Installs vary widely
plt.ylim(0,5)
plt.title("Rating vs Number of Installs")
plt.xlabel("Number of Installs (Log Scale)")
plt.ylabel("Rating")
plt.show()

# -----------------------------
# 2️⃣ Price vs Installs
# -----------------------------
plt.figure(figsize=(10,6))
sns.scatterplot(x='Installs', y='Price', data=df, alpha=0.5, color='orange')
plt.xscale('log')
plt.ylim(0, 50)  # Limit to remove extreme outliers
plt.title("Price vs Number of Installs")
plt.xlabel("Number of Installs (Log Scale)")
plt.ylabel("Price ($)")
plt.show()

# -----------------------------
# 3️⃣ Reviews vs Rating
# -----------------------------
plt.figure(figsize=(10,6))
sns.scatterplot(x='Reviews', y='Rating', data=df, alpha=0.5, color='green')
plt.xscale('log')
plt.ylim(0,5)
plt.title("Number of Reviews vs Rating")
plt.xlabel("Number of Reviews (Log Scale)")
plt.ylabel("Rating")
plt.show()

# -----------------------------
# 4️⃣ Correlation Coefficients
# -----------------------------
numeric_cols = ['Rating', 'Reviews', 'Installs', 'Price']
corr_matrix = df[numeric_cols].corr()
print("Correlation between variables:\n", corr_matrix)