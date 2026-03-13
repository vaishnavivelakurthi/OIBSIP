import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 2 level 2\WineQT.csv")  # replace with your dataset path

# 1. Correlation Heatmap
plt.figure(figsize=(12,8))
corr = df.corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Heatmap of Wine Features")
plt.show()

# 2. Pair Plot (can be cluttered with 11 features)
sns.pairplot(df, vars=df.columns[:-1], hue='quality', palette='coolwarm', corner=True)
plt.suptitle("Pair Plot of Wine Features (may be cluttered)", y=1.02)
plt.show()