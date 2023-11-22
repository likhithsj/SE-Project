import json
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

# Read data from JSON files
def read_data_from_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

# Read data from JSON files
bug_texts = read_data_from_json("snapshot_20230831/bug.json")["bug"]
theory_question_texts = read_data_from_json("snapshot_20230831/theory_question_data.json")["theory_question"]
feature_request_texts = read_data_from_json("snapshot_20230831/feature_request_data.json")["feature_request"]

# Combine texts and labels
texts = bug_texts + theory_question_texts + feature_request_texts
labels = ["bug"] * len(bug_texts) + ["theory_question"] * len(theory_question_texts) + ["feature_request"] * len(feature_request_texts)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# Convert text data to numerical features using TF-IDF
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train_tfidf, y_train)

# Make predictions on the test set
predictions = classifier.predict(X_test_tfidf)

# Evaluate the performance of the model
accuracy = metrics.accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")

# Example usage: classify a new text
new_text = "how to make a commit in github"
new_text_tfidf = vectorizer.transform([new_text])
prediction = classifier.predict(new_text_tfidf)
print(f"Predicted category for the new text: {prediction}")



















































# # Import necessary libraries
# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.naive_bayes import MultinomialNB
# from sklearn import metrics

# # Sample data (replace this with your labeled dataset)
# texts = ["This is a bug in the system.", 
#          "I have a question about the theory.", 
#          "Please implement this new feature.", 
#          "There is an issue with the login functionality."]

# labels = ["bug", "theory question", "feature request", "issue"]

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# # Convert text data to numerical features using TF-IDF
# vectorizer = TfidfVectorizer()
# X_train_tfidf = vectorizer.fit_transform(X_train)
# X_test_tfidf = vectorizer.transform(X_test)

# # Train a Naive Bayes classifier
# classifier = MultinomialNB()
# classifier.fit(X_train_tfidf, y_train)

# # Make predictions on the test set
# predictions = classifier.predict(X_test_tfidf)

# # Evaluate the performance of the model
# accuracy = metrics.accuracy_score(y_test, predictions)
# print(f"Accuracy: {accuracy}")

# # Example usage: classify a new text
# new_text = "implement"
# new_text_tfidf = vectorizer.transform([new_text])
# prediction = classifier.predict(new_text_tfidf)
# print(f"Predicted category for the new text: {prediction}")