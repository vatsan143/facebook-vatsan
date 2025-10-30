
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download NLTK resources 
nltk.download('vader_lexicon')

# Load the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Example Facebook data 
facebook_data = [
  "I love the new feature! It's amazing.",
  "The service was terrible. I'm very disappointed.",
  "Great job on the update!",
  "The product quality is poor. I won't be buying again.",
  
]

# Perform sentiment analysis and filter for negative feedback
negative_feedback = []

for message in facebook_data:
  sentiment_score = sia.polarity_scores(message)['compound']
  if sentiment_score < 0:  # Negative sentiment
      negative_feedback.append(message)

# Print the negative feedback
print("Negative Feedback:")
for feedback in negative_feedback:
  print(feedback)