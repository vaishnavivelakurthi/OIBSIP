import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("retails_sales_cleaned.csv")

# ---------------------------------------------------------
# 1. CUSTOMER BEHAVIOR ANALYSIS
# ---------------------------------------------------------

# 📌 Total spending by each customer
customer_spending = df.groupby("Customer ID")["Total Amount"].sum().sort_values(ascending=False)
print("\n📌 Top Customer Spending:")
print(customer_spending.head())

# 📌 Gender-based spending
gender_spending = df.groupby("Gender")["Total Amount"].sum()
print("\n📌 Gender-wise Total Spending:")
print(gender_spending)

# 📌 Average order value by gender
avg_gender_spending = df.groupby("Gender")["Total Amount"].mean()
print("\n📌 Average Spending Per Purchase (Gender):")
print(avg_gender_spending)

# 📌 Create age groups to analyze spending behavior
bins = [18, 30, 40, 50, 60, 100]
labels = ["18-30", "31-40", "41-50", "51-60", "60+"]
df["Age Group"] = pd.cut(df["Age"], bins=bins, labels=labels, right=False)

age_group_spending = df.groupby("Age Group")["Total Amount"].sum()
print("\n📌 Spending by Age Group:")
print(age_group_spending)

# ---------------------------------------------------------
# 2. PRODUCT BEHAVIOR ANALYSIS
# ---------------------------------------------------------

# 📌 Total sales by product category
category_sales = df.groupby("Product Category")["Total Amount"].sum()
print("\n📌 Total Revenue by Product Category:")
print(category_sales)

# 📌 Best-selling categories (quantity sold)
category_quantity = df.groupby("Product Category")["Quantity"].sum()
print("\n📌 Quantity Sold by Product Category:")
print(category_quantity)

# 📌 Average price per product category
avg_price_cat = df.groupby("Product Category")["Price per Unit"].mean()
print("\n📌 Average Price per Category:")
print(avg_price_cat)

# 📌 Find top 10 highest revenue transactions
top_transactions = df.sort_values("Total Amount", ascending=False).head(10)
print("\n📌 Top 10 Highest Revenue Transactions:")
print(top_transactions)

# ---------------------------------------------------------
# 3. VISUALIZATIONS (OPTIONAL, VERY USEFUL)
# ---------------------------------------------------------

# -------- Gender Spending Bar Chart --------
plt.figure(figsize=(6,4))
plt.bar(gender_spending.index, gender_spending.values)
plt.title("Total Spending by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Amount")
plt.show()

# -------- Age Group Spending --------
plt.figure(figsize=(7,4))
plt.bar(age_group_spending.index.astype(str), age_group_spending.values)
plt.title("Spending by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Total Amount")
plt.show()

# -------- Category Revenue Bar Chart --------
plt.figure(figsize=(7,4))
plt.bar(category_sales.index, category_sales.values)
plt.title("Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Revenue")
plt.show()

# ---------------------------------------------------------
print("\n✔ Customer & Product Behavior Analysis Completed!")