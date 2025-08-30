# Behavioral-Analysis-Chat
This project, Behavioral Analysis Chat, is a Python-based tool designed to analyze conversation data from a text file named export.txt. It offers two distinct methods for understanding the content, progressing from a simple word-matching approach to a more complex sentiment analysis.

Version 1: Keyword Search 🕵️
This initial version is a straightforward keyword search tool. Its primary function is to efficiently scan through a chat log to find and count specific words or phrases you define. It reads the file line by line and identifies all occurrences of your search terms, regardless of capitalization. This is ideal for quickly locating every instance of a particular topic, name, or phrase within a large conversation.

Version 2: Sentiment Analysis 🧠
The second version is a more advanced sentiment analysis tool. Instead of just looking for specific words, this script uses a natural language processing model from the NLTK library to analyze the emotional tone of each message. It provides a numerical breakdown of the text's sentiment, including scores for:

Positive: The percentage of positive emotion detected.

Negative: The percentage of negative emotion detected.

Neutral: The percentage of neutral tone detected.

Compound: An overall, normalized score that gives a single value for the message's emotional intensity.
