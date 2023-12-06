import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

def load_json_data(json_files):
    """Load data from the specified JSON files."""
    dfs = []
    for file_name in json_files:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
            df = pd.json_normalize(data, record_path=['Chats'])
            dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

def calculate_length(text):
    """Calculate the length of the text in terms of number of words."""
    return len(text.split())

def analyze_lengths(dataset):
    """Perform analysis on the lengths of questions and responses."""
    dataset['question_length'] = dataset['question'].apply(calculate_length)
    dataset['response_length'] = dataset['response'].apply(calculate_length)
    
    correlation, p_value = pearsonr(dataset['question_length'], dataset['response_length'])
    print(f'Pearson correlation: {correlation}, P-value: {p_value}')

    return dataset

def visualize_data(dataset):
    """Visualize the relationship between question and response lengths."""
    sns.scatterplot(x='question_length', y='response_length', data=dataset)
    plt.xlabel('Question Length (words)')
    plt.ylabel('Response Length (words)')
    plt.title('Question Length vs Response Length')
    plt.show()

def main():
    # List of JSON files to load (update this list with your actual files)
    json_files = ['commitsharing.json', 'discussions.json', 'filesharing.json', 'hnsharing.json', 'issuesharing.json', 'prsharing.json']

    # Load dataset
    dataset = load_json_data(json_files)
    # load data based on the fixed format
    dataset.rename(columns={'Prompt': 'question', 'Answer': 'response'}, inplace=True)

    # Data Validation: Print the first few rows to check the data
    # print(dataset.head())

    # Analyze lengths
    analyzed_dataset = analyze_lengths(dataset)

    # Visualization
    visualize_data(analyzed_dataset)

if __name__ == "__main__":
    main()
