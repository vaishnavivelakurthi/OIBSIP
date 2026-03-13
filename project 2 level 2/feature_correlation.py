# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv(r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 2 level 2\WineQT.csv")  # Replace with your file path

# 1. Check correlations
correlation_matrix = df.corr()
print("Correlation Matrix:\n", correlation_matrix['quality'].sort_values(ascending=False))

# 2. Visualize correlations with heatmap
plt.figure(figsize=(12,8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.show()

# 3. Feature scaling for PCA
features = df.drop('quality', axis=1)
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# 4. Apply PCA
pca = PCA(n_components=0.95)  # Keep 95% variance
pca_components = pca.fit_transform(features_scaled)

print("\nOriginal number of features:", features.shape[1])
print("Number of features after PCA:", pca_components.shape[1])