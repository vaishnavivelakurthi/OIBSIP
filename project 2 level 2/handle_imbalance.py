# File name: handle_imbalance.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
from imblearn.over_sampling import SMOTE

# Load dataset
df = pd.read_csv(r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 2 level 2\WineQT.csv")

# --- 1. Check class distribution ---
print("Class distribution in 'quality':")
print(df['quality'].value_counts())

# --- 2. Visualize imbalance ---
plt.figure(figsize=(10,6))
sns.countplot(x='quality', data=df)
plt.title("Distribution of Wine Quality Scores")
plt.show()

# --- 3. Handle Imbalance using SMOTE ---
X = df.drop("quality", axis=1)
y = df["quality"]

print("\nOriginal class distribution:", Counter(y))

smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X, y)

print("Resampled class distribution:", Counter(y_res))

# Optional: Convert back to a dataframe
df_resampled = pd.concat([pd.DataFrame(X_res, columns=X.columns), pd.DataFrame(y_res, columns=['quality'])], axis=1)
print("\nFirst 5 rows of resampled dataset:")
print(df_resampled.head())