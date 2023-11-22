"""
The script calculates the cosine similarity between each prompt 
and its corresponding answer. Cosine similarity is a common measure 
for comparing text similarity in natural language processing.
"""
import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load JSON data
json_files = ['commitsharing.json', 'discussions.json', 'filesharing.json', 'hnsharing.json', 'issuesharing.json', 'prsharing.json']
dfs = [] #initialize an empty list to store dataframes

#loop through each file and load data
for file_name in json_files:
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
        df = pd.json_normalize(data, record_path = ['Chats'])
        dfs.append(df)

# Concatenate all DataFrames into one
df = pd.concat(dfs, ignore_index=True)

# Ensure text is in string format
df['Prompt'] = df['Prompt'].astype(str)
df['Answer'] = df['Answer'].astype(str)

# Calculate length of prompts and responses
df['Prompt_Length'] = df['Prompt'].apply(len)
df['Answer_Length'] = df['Answer'].apply(len)

# More features can be added here, such as complexity, specific keywords, etc.

# Create a TfidfVectorizer
# TF-IDF: term frequency-inverse document frequency
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
