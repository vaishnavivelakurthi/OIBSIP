import pandas as pd
import matplotlib
matplotlib.use("TkAgg")  # Ensures charts open properly in VS Code
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------
# ✅ Load Data
# ----------------------------------------
df = pd.read_csv(r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 1 level 1\retails_sales_cleaned.csv")   # Make sure file is in the same folder

# ----------------------------------------
# 📌 Bar Chart: Revenue by Product Category
# ----------------------------------------
category_sales = df.groupby("Product Category")["Total Amount"].sum().reset_index()

plt.figure(figsize=(8,5))
sns.barplot(data=category_sales, x="Product Category", y="Total Amount")
plt.title("Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.show(block=True)

# ----------------------------------------
# 📌 Bar Chart: Customer Count by Gender
# ----------------------------------------
gender_count = df["Gender"].value_counts().reset_index()
gender_count.columns = ["Gender", "Count"]

plt.figure(figsize=(6,4))
sns.barplot(data=gender_count, x="Gender", y="Count")
plt.title("Customer Count by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.tight_layout()
plt.show(block=True)

# ----------------------------------------
# 📌 Line Chart: Sales Trend Over Time
# ----------------------------------------
df["Date"] = pd.to_datetime(df["Date"])  # convert date

daily_sales = df.groupby("Date")["Total Amount"].sum().reset_index()

plt.figure(figsize=(10,4))
plt.plot(daily_sales["Date"], daily_sales["Total Amount"])
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show(block=True)

# ----------------------------------------
# 📌 Heatmap: Correlation Matrix
# ----------------------------------------
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show(block=True)