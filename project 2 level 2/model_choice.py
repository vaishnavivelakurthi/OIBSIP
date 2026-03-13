# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, accuracy_score

# Load dataset
df = pd.read_csv(r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 2 level 2\WineQT.csv") # Replace with your file path

# Option 1: Regression (predict exact quality)
X = df.drop('quality', axis=1)
y_reg = df['quality']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y_reg, test_size=0.2, random_state=42)

# Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_reg = lr.predict(X_test)
mse = mean_squared_error(y_test, y_pred_reg)
print("Regression - Linear Regression MSE:", mse)

# Option 2: Classification (group quality into Low, Medium, High)
# Define bins: Low (3-5), Medium (6-7), High (8-9)
y_clf = pd.cut(df['quality'], bins=[2,5,7,10], labels=['Low','Medium','High'])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y_clf, test_size=0.2, random_state=42)

# Logistic Regression
logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train, y_train)
y_pred_clf = logreg.predict(X_test)
acc = accuracy_score(y_test, y_pred_clf)
print("Classification - Logistic Regression Accuracy:", acc)