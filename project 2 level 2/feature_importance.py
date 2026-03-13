# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 2 level 2\WineQT.csv")  # replace with your path

# Features and target
X = df.drop('quality', axis=1)
y = df['quality']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 1. Linear Regression (interpretable coefficients)
lr = LinearRegression()
lr.fit(X_train, y_train)
coefficients = pd.Series(lr.coef_, index=X.columns).sort_values(key=abs, ascending=False)
print("Linear Regression Feature Coefficients:\n", coefficients)

# 2. Random Forest (tree-based importance)
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
importances = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\nRandom Forest Feature Importances:\n", importances)

# Visualization
plt.figure(figsize=(10,6))
sns.barplot(x=importances.values, y=importances.index)
plt.title("Feature Importance (Random Forest)")
plt.show()