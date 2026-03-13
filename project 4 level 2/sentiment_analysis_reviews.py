# File: sentiment_analysis_reviews.py

import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

# Download NLTK resources (only first time)
nltk.download('stopwords')
nltk.download('vader_lexicon')

# Load dataset
df = pd.read_csv(r"C:\Users\Vaishnavi\OneDrive\Desktop\Data Analytics\project 4 level 2\user_reviews.csv")

print("Original Dataset Shape:", df.shape)

# Remove missing reviews
df = df.dropna(subset=['Translated_Review'])

# Convert reviews to string
df['Translated_Review'] = df['Translated_Review'].astype(str)

# Load stopwords
stop_words = set(stopwords.words('english'))

# Function to clean text
def clean_text(text):

    # Convert to lowercase
    text = text.lower()

    # Remove special characters & numbers
    text = re.sub(r'[^a-z\s]', '', text)

    # Remove stopwords
    words = text.split()
    words = [word for word in words if word not in stop_words]

    return " ".join(words)

# Apply cleaning
df['Cleaned_Review'] = df['Translated_Review'].apply(clean_text)

print("\nSample Cleaned Reviews:\n")
print(df[['Translated_Review','Cleaned_Review']].head())

# Sentiment Analysis using VADER
sia = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = sia.polarity_scores(text)['compound']
    
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

df['Predicted_Sentiment'] = df['Cleaned_Review'].apply(get_sentiment)

# Sentiment count
sentiment_counts = df['Predicted_Sentiment'].value_counts()

print("\nSentiment Distribution:\n")
print(sentiment_counts)

# Save output
df.to_csv("cleaned_reviews_sentiment.csv", index=False)

print("\nFile saved as: cleaned_reviews_sentiment.csv")