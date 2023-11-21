import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load JSON data
with open('your_json_file.json', 'r') as file:
    data = json.load(file)

# Convert to DataFrame
df = pd.json_normalize(data, record_path=['Chats'])

# Ensure text is in string format
df['Prompt'] = df['Prompt'].astype(str)
df['Answer'] = df['Answer'].astype(str)

# Calculate length of prompts and responses
df['Prompt_Length'] = df['Prompt'].apply(len)
df['Answer_Length'] = df['Answer'].apply(len)

# More features can be added here, such as complexity, specific keywords, etc.

# Create a TfidfVectorizer
vectorizer = TfidfVectorizer()

# Combine Prompts and Answers for TF-IDF
combined_text = df['Prompt'].tolist() + df['Answer'].tolist()

# Fit and transform the text
tfidf_matrix = vectorizer.fit_transform(combined_text)

# Split the matrix back into prompts and answers
half_way = len(df['Prompt'])
prompt_tfidf = tfidf_matrix[:half_way]
answer_tfidf = tfidf_matrix[half_way:]

# Calculate cosine similarity
cos_sim = [cosine_similarity(prompt_tfidf[i], answer_tfidf[i])[0][0] for i in range(half_way)]

# Add to DataFrame
df['Cosine_Similarity'] = cos_sim

# Perform some basic statistical analysis
# For example, correlation between prompt length and similarity score
correlation = df[['Prompt_Length', 'Cosine_Similarity']].corr()

print(correlation)
