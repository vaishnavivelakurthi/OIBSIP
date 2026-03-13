import pandas as pd

# Load data
df = pd.read_csv("retails_sales_cleaned"
".csv")
df["Date"] = pd.to_datetime(df["Date"])

# -------------------------------
# 📌 1. Overall Business Summary
# -------------------------------
total_revenue = df["Total Amount"].sum()
avg_order_value = df["Total Amount"].mean()
total_transactions = len(df)

print("📌 BUSINESS SUMMARY:")
print(f"Total Revenue: ₹{total_revenue}")
print(f"Average Order Value: ₹{avg_order_value:.2f}")
print(f"Total Transactions: {total_transactions}")

# -------------------------------
# 📌 2. Top Product Insights
# -------------------------------
category_revenue = df.groupby("Product Category")["Total Amount"].sum()
best_category = category_revenue.idxmax()
worst_category = category_revenue.idxmin()

print("\n📌 PRODUCT INSIGHTS:")
print("Revenue by category:")
print(category_revenue)
print(f"Best Category: {best_category}")
print(f"Weakest Category: {worst_category}")

# -------------------------------
# 📌 3. Customer Insights
# -------------------------------
gender_spending = df.groupby("Gender")["Total Amount"].sum()
age_avg_spending = df.groupby("Age")["Total Amount"].mean()

top_customers = df.groupby("Customer ID")["Total Amount"].sum().sort_values(ascending=False).head(5)

print("\n📌 CUSTOMER INSIGHTS:")
print("Gender-wise spending:")
print(gender_spending)
print("\nTop 5 High-Value Customers:")
print(top_customers)

# -------------------------------
# 📌 4. Time-Based Insights
# -------------------------------
df["Month"] = df["Date"].dt.month
monthly_sales = df.groupby("Month")["Total Amount"].sum()

best_month = monthly_sales.idxmax()
worst_month = monthly_sales.idxmin()

print("\n📌 TIME ANALYSIS:")
print("Monthly Revenue:")
print(monthly_sales)
print(f"Best Month for Sales: {best_month}")
print(f"Weakest Month for Sales: {worst_month}")

# -------------------------------
# 📌 5. Operational Insights
# -------------------------------
quantity_sold = df.groupby("Product Category")["Quantity"].sum()
returns_issue = df[df["Quantity"] == 1].shape[0]

print("\n📌 OPERATIONS INSIGHTS:")
print("Quantity sold per category:")
print(quantity_sold)
print(f"Transactions with only 1 item (may indicate lost upsell opportunities): {returns_issue}")