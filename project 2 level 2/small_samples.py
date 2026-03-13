import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 2 level 2\WineQT.csv")  # Replace with your dataset path

# Select features to analyze extremes
features = ['alcohol', 'pH', 'residual sugar']

for feature in features:
    plt.figure(figsize=(8,5))
    sns.histplot(df[feature], bins=30, kde=True, color='skyblue')
    plt.title(f'Distribution of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Count')
    plt.show()

    # Identify extreme ranges (approx. top/bottom 5%)
    lower_extreme = df[feature].quantile(0.05)
    upper_extreme = df[feature].quantile(0.95)
    extremes_count = df[(df[feature] < lower_extreme) | (df[feature] > upper_extreme)].shape[0]
    print(f"{feature}: {extremes_count} samples in extreme ranges ({lower_extreme:.2f} - {upper_extreme:.2f})")