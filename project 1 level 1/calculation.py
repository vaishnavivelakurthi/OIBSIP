import pandas as pd

# Load cleaned dataset
df = pd.read_csv("retails_sales_cleaned.csv")

# ------------------------------------------
# 1. BASIC DESCRIPTIVE STATISTICS
# ------------------------------------------
print("📌 Basic Statistics:")
print(df.describe())

# ------------------------------------------
# 2. MEAN (Average Values)
# ------------------------------------------
print("\n📌 Mean Values:")
print("Average Age:", df['Age'].mean())
print("Average Quantity:", df['Quantity'].mean())
print("Average Price per Unit:", df['Price per Unit'].mean())
print("Average Total Amount:", df['Total Amount'].mean())

# ------------------------------------------
# 3. MEDIAN (Middle Value)
# ------------------------------------------
print("\n📌 Median Values:")
print("Median Age:", df['Age'].median())
print("Median Quantity:", df['Quantity'].median())
print("Median Price per Unit:", df['Price per Unit'].median())
print("Median Total Amount:", df['Total Amount'].median())

# ------------------------------------------
# 4. MODE (Most Frequent Value)
# ------------------------------------------
print("\n📌 Mode Values:")
print("Most Common Gender:", df['Gender'].mode()[0])
print("Most Common Product Category:", df['Product Category'].mode()[0])
print("Most Common Quantity:", df['Quantity'].mode()[0])

# ------------------------------------------
# 5. STANDARD DEVIATION (How Spread Out Values Are)
# ------------------------------------------
print("\n📌 Standard Deviation:")
print("Age Std Dev:", df['Age'].std())
print("Quantity Std Dev:", df['Quantity'].std())
print("Price per Unit Std Dev:", df['Price per Unit'].std())
print("Total Amount Std Dev:", df['Total Amount'].std())

# ------------------------------------------
# 6. MINIMUM & MAXIMUM VALUES
# ------------------------------------------
print("\n📌 Min & Max Values:")
print("Minimum Age:", df['Age'].min())
print("Maximum Age:", df['Age'].max())
print("Minimum Total Amount:", df['Total Amount'].min())
print("Maximum Total Amount:", df['Total Amount'].max())

# ------------------------------------------
# 7. GROUP-WISE STATISTICS
# ------------------------------------------

# Average spending by gender
print("\n📌 Average Total Amount by Gender:")
print(df.groupby('Gender')['Total Amount'].mean())

# Average quantity purchased by product category
print("\n📌 Average Quantity by Product Category:")
print(df.groupby('Product Category')['Quantity'].mean())

# Total revenue by product category
print("\n📌 Total Revenue by Product Category:")
print(df.groupby('Product Category')['Total Amount'].sum())

# ------------------------------------------
print("\n✔ Meaningful statistics calculated successfully!")