from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,classification_report

text = [
"I loved this movie",
"I hate this movie",
"Amazing acting by allu arjun",
"Stylish star alluarjun",
"This is the best movie ever",
"worst direction",
"Not much worthy acting with co-actors",
"Love allu arjun movie",
"This is the best movie ever", 
"What a boring film", 
"Terrible screenplay", 
"I enjoyed every minute", 
"Superb acting", 
"Pathetic acting", 
"The plot was predictable", 
"Outstanding visual effects", 
"It was a waste of time", 
"I won't watch it again",
"Let's watch the movie once again",
"Best movie ever",
"Awesome dailogue & acting",
"Worst movie"
]
label = [
1,0,1,1,1,0,0,1,1,0, 0, 1, 1, 0, 1, 0, 0, 0,1,1,1,0
]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(text)
x_train, x_test, y_train, y_test = train_test_split(X,label,test_size=0.12,random_state=20)
nb = MultinomialNB()
nb.fit(x_train,y_train) #train--
y_predict = nb.predict(x_test) #test
acc = accuracy_score(y_test,y_predict)
print(f"Accuracy: {100*acc:.2f}%")
print("Classification report : ")
print(classification_report(y_test,y_predict,target_names = ["Negative","Positive"]))
#Testing the trained model:
new_text = ["The Best movie"]
new_text_tranform = vectorizer.transform(new_text)
p = nb.predict(new_text_tranform)
print(f"Prediction for {new_text}: ", "Positive" if p[0] == 1 else "Negative")