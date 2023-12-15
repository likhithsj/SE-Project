import nltk
nltk.download('stopwords')
import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud


# Specify the path to your JSON file
json_file_path = 'snapshot_20230831/prsharing.json'

# Load JSON data from the file with explicit encoding
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract the "chats" array
chats = data.get("chats", [])
chats = [' '.join(map(str, chat)) for chat in chats]
all_text = ' '.join(chats)


# Tokenize each conversation
tokenized_conversations = [word_tokenize(chat) for chat in chats]

# Define a list of programming language keywords

programming_keywords = ["python", "java", "javascript", "c++", "ruby", "html", "css", "php", "swift", "typescript", "sql", "scala", "go", "rust", "kotlin"]


stop_words = set(stopwords.words('english'))

# Remove stopwords and non-programming words from each conversation
filtered_conversations = [
    [word.lower() for word in chat if word.lower() not in stop_words and word.isalpha() and word.lower() in programming_keywords]
    for chat in tokenized_conversations
]

# Flatten the list of words
all_words = [word for chat in filtered_conversations for word in chat]

# Count the frequency of each word
word_freq = Counter(all_words)

# Print the most common words
print("Most common words:", word_freq.most_common(10))

# Visualize word frequencies with a bar chart
plt.bar(*zip(*word_freq.most_common(10)))
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 10 Most Common Programming Language Words')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels
plt.tight_layout()  # Adjust layout for better readability
plt.show()

# Visualize word frequencies with a word cloud
wordcloud = WordCloud(width=800, height=400, random_state=21, max_font_size=110).generate_from_frequencies(word_freq)
plt.figure(figsize=(10, 7))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')
plt.show()
