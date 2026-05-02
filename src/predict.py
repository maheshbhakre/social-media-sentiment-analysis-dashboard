import joblib

model = joblib.load('../models/sentiment_model.pkl')
vectorizer = joblib.load('../models/vectorizer.pkl')

text = input("Enter Text: ")

text_vector = vectorizer.transform([text])

prediction = model.predict(text_vector)

print("Predicted Sentiment:", prediction[0])