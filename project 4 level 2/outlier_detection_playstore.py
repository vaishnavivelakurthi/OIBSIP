import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 4 level 2\apps.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Print column names to verify
print("Columns in dataset:")
print(df.columns)

print("\nOriginal Dataset Shape:", df.shape)

# Convert Installs column
df['Installs'] = df['Installs'].astype(str)
df['Installs'] = df['Installs'].str.replace(',', '')
df['Installs'] = df['Installs'].str.replace('+', '')
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

# Convert Price column
df['Price'] = df['Price'].astype(str)
df['Price'] = df['Price'].str.replace('$', '')
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# Convert Size column
df['Size'] = df['Size'].astype(str)
df['Size'] = df['Size'].str.replace('M', '')
df['Size'] = df['Size'].str.replace('k', '')
df['Size'] = df['Size'].str.replace('Varies with device', '0')
df['Size'] = pd.to_numeric(df['Size'], errors='coerce')

# Function to remove outliers
def remove_outliers(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    return data[(data[column] >= lower) & (data[column] <= upper)]

# Remove outliers
df = remove_outliers(df, 'Price')
df = remove_outliers(df, 'Installs')
df = remove_outliers(df, 'Size')

print("Dataset Shape After Removing Outliers:", df.shape)

# Save cleaned dataset
df.to_csv("playstore_no_outliers.csv", index=False)

print("Cleaned file saved as: playstore_no_outliers.csv")