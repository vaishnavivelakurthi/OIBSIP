import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 2 level 2\WineQT.csv") # Replace with your file path

# 1. Check distribution of quality scores
plt.figure(figsize=(8,5))
sns.countplot(x='quality', data=df, palette='coolwarm')
plt.title("Distribution of Wine Quality Scores")
plt.show()

# 2. Analyze variance within features per quality score
feature = 'alcohol'  # example numeric feature
plt.figure(figsize=(8,5))
sns.boxplot(x='quality', y=feature, data=df, palette='coolwarm')
plt.title(f"{feature} Distribution Across Quality Scores")
plt.show()

# 3. Optional: Identify possible outlier/noisy quality ratings
# High variance within a score may indicate subjectivity/noise
variance_per_quality = df.groupby('quality').var()
print("Variance of features per quality score:\n", variance_per_quality)