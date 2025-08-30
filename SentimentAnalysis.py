import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_chat_with_ai(file_path):
    sia = SentimentIntensityAnalyzer()
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                # Use the AI model to get sentiment scores
                sentiment_scores = sia.polarity_scores(line)
                
                # Print the line and its sentiment
                print(f"Chat: '{line}'")
                print(f"Sentiment: {sentiment_scores}")
                print("-" * 20)

if __name__ == "__main__":
    file_path = "export.txt"
    analyze_chat_with_ai(file_path)
