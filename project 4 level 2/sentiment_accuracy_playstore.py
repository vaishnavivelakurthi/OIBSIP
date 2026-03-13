import pandas as pd
import re
from textblob import TextBlob

# Load user reviews dataset
reviews_df = pd.read_csv(r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 4 level 2\user_reviews.csv")

# Strip column names
reviews_df.columns = reviews_df.columns.str.strip()

# Display first few rows
print(reviews_df.head())

# -----------------------------
# 1️⃣ Basic Cleaning
# -----------------------------
def clean_text(text):
    if pd.isna(text):
        return ""
    # Remove special characters, emojis, and extra spaces
    text = re.sub(r'[^A-Za-z0-9\s]+', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

reviews_df['cleaned_review'] = reviews_df['Translated_Review'].apply(clean_text)

# -----------------------------
# 2️⃣ Sentiment Analysis with TextBlob
# -----------------------------
def get_sentiment(text):
    if text == "":
        return "neutral"
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

reviews_df['predicted_sentiment'] = reviews_df['cleaned_review'].apply(get_sentiment)

# -----------------------------
# 3️⃣ Compare with Original Sentiment
# -----------------------------
if 'Sentiment' in reviews_df.columns:
    total = len(reviews_df)
    correct = (reviews_df['Sentiment'].str.lower() == reviews_df['predicted_sentiment']).sum()
    accuracy = (correct / total) * 100
    print(f"Approximate Sentiment Accuracy: {accuracy:.2f}%")
else:
    print("Original sentiment labels not found. Only predicted sentiments are available.")

# -----------------------------
# 4️⃣ Sample Output
# -----------------------------
print(reviews_df[['Translated_Review', 'cleaned_review', 'predicted_sentiment']].head(10))