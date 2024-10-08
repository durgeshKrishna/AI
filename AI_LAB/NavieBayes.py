from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,classification_report
texts = [
    "I love this movie", 
    "This is a great film", 
    "Amazing performance", 
    "I hate this movie", 
    "This is a terrible film", 
    "Worst acting", 
    "Fantastic direction", 
    "Wonderful storyline", 
    "Brilliant cinematography", 
    "Horrible dialogue", 
    "This is the best movie ever", 
    "What a boring film", 
    "Terrible screenplay", 
    "I enjoyed every minute", 
    "Superb acting", 
    "Pathetic acting", 
    "The plot was predictable", 
    "Outstanding visual effects", 
    "It was a waste of time", 
    "I would watch it again"
]
labels = [
    1, 1, 1, 0, 0, 0, 
    1, 1, 1, 0, 1, 
    0, 0, 1, 1, 0, 
    1, 0, 1,1
]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.25, random_state=32)
nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)
y_pred = nb_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
new_text = ["I love the acting"]
new_text_transformed = vectorizer.transform(new_text)
prediction = nb_model.predict(new_text_transformed)
target_names = ["Negative", "Positive"]
print("Prediction for the new text:", "Positive" if prediction[0] == 1 else "Negative")
report = classification_report(y_test, y_pred, target_names=target_names)
print("Classification Report:")
print(report)
