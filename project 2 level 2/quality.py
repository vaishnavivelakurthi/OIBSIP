import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 2 level 2\WineQT.csv") # Replace with your file path
 # Replace with your dataset path

# Define buckets
def quality_category(q):
    if q <= 4:
        return 'Bad'
    elif q <= 6:
        return 'Average'
    else:
        return 'Good'

# Apply transformation
df['quality_label'] = df['quality'].apply(quality_category)

# Check class distribution
print(df['quality_label'].value_counts())

# Visualize
plt.figure(figsize=(6,4))
sns.countplot(x='quality_label', data=df, palette='Set2')
plt.title('Wine Quality Category Distribution')
plt.show()