# Import libraries
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt

# -------------------------------
# 1️⃣ Load dataset
# -------------------------------
file_path = r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 3 level 2\creditcard.csv"

if not os.path.exists(file_path):
    raise FileNotFoundError(f"File not found at {file_path}. Please check the path!")

df = pd.read_csv(file_path)
print("CSV loaded successfully!")
print("Dataset shape:", df.shape)
print("Columns:", df.columns.tolist())

# -------------------------------
# 2️⃣ Handle class imbalance with SMOTE
# -------------------------------
X = df.drop("Class", axis=1)
y = df["Class"]

smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X, y)

df_balanced = pd.concat([X_res, y_res], axis=1)
balanced_path = r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 3 level 2\balanced_creditcard_train.csv"
df_balanced.to_csv(balanced_path, index=False)
print(f"Balanced dataset created and saved at: {balanced_path}")
print("Balanced dataset shape:", df_balanced.shape)

# -------------------------------
# 3️⃣ Split dataset into train/test
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_res, y_res, test_size=0.2, random_state=42, stratify=y_res
)

# -------------------------------
# 4️⃣ Train Random Forest and get feature importance
# -------------------------------
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

importances = rf.feature_importances_
feature_names = X.columns
feature_importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importances
}).sort_values(by="Importance", ascending=False)

print("\nTop 10 important features:")
print(feature_importance_df.head(10))

# -------------------------------
# 5️⃣ Optional: Visualize feature importance
# -------------------------------
plt.figure(figsize=(12,6))
plt.bar(feature_importance_df['Feature'], feature_importance_df['Importance'])
plt.xticks(rotation=90)
plt.title("Feature Importance from Random Forest")
plt.tight_layout()
plt.show()

# -------------------------------
# 6️⃣ Select top 10 features and save
# -------------------------------
top_features = feature_importance_df['Feature'].head(10).tolist()
X_train_top = X_train[top_features]
X_test_top = X_test[top_features]

selected_features_train = pd.concat([X_train_top, y_train.reset_index(drop=True)], axis=1)
top_features_path = r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 3 level 2\selected_features_train.csv"
selected_features_train.to_csv(top_features_path, index=False)
print(f"\nTop features dataset saved at: {top_features_path}")