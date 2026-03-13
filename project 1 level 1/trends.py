import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("retails_sales_cleaned.csv")

# ----------------------------------------------------
# 1. CONVERT DATE COLUMN TO DATETIME
# ----------------------------------------------------
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# ----------------------------------------------------
# 2. CREATE NEW TIME COLUMNS (YEAR, MONTH)
# ----------------------------------------------------
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Month_Name'] = df['Date'].dt.strftime("%B")

# ----------------------------------------------------
# 3. DAILY SALES TREND
# ----------------------------------------------------
daily_sales = df.groupby('Date')['Total Amount'].sum()

print("\n📌 Daily Sales Trend:")
print(daily_sales.head())

# ----------------------------------------------------
# 4. MONTHLY SALES TREND
# ----------------------------------------------------
monthly_sales = df.groupby(['Year', 'Month'])['Total Amount'].sum()

print("\n📌 Monthly Sales Trend:")
print(monthly_sales)

# ----------------------------------------------------
# 5. PLOT DAILY SALES TREND
# ----------------------------------------------------
plt.figure(figsize=(12,6))
plt.plot(daily_sales.index, daily_sales.values)
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales Amount")
plt.grid(True)
plt.tight_layout()
plt.show()

# ----------------------------------------------------
# 6. PLOT MONTHLY SALES TREND
# ----------------------------------------------------
monthly_sales_plot = monthly_sales.reset_index()
monthly_sales_plot['Year-Month'] = monthly_sales_plot['Year'].astype(str) + "-" + monthly_sales_plot['Month'].astype(str)

plt.figure(figsize=(12,6))
plt.plot(monthly_sales_plot['Year-Month'], monthly_sales_plot['Total Amount'])
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales Amount")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# ----------------------------------------------------
# 7. IDENTIFY BEST & WORST MONTHS
# ----------------------------------------------------
best_month = monthly_sales.idxmax()
worst_month = monthly_sales.idxmin()

print("\n📌 Best Month for Sales:", best_month, "→", monthly_sales.max())
print("📌 Worst Month for Sales:", worst_month, "→", monthly_sales.min())