# File name: fraud_smote_balance.py

# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from collections import Counter

# Load dataset
# Make sure your CSV file is in the same folder or provide full path
df = pd.read_csv(r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 3 level 2\creditcard.csv")  # Replace with your actual file name

# Check initial class distribution
print("Original class distribution:")
print(df['Class'].value_counts())

# Separate features and target
X = df.drop('Class', axis=1)
y = df['Class']

# Split into train and test (optional but recommended)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Apply SMOTE to training data
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

# Check new class distribution after SMOTE
print("\nResampled class distribution:")
print(Counter(y_train_res))

# Save the balanced dataset to CSV
balanced_train = pd.concat([pd.DataFrame(X_train_res, columns=X.columns),
                            pd.DataFrame(y_train_res, columns=['Class'])], axis=1)
balanced_train.to_csv("balanced_creditcard_train.csv", index=False)

print("\nBalanced training data saved as 'balanced_creditcard_train.csv'")