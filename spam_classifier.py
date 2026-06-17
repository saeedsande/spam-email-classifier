import joblib

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

spam_keywords = [
    "win", "prize", "free", "cash",
    "offer", "urgent", "click",
    "reward", "money", "lottery",
    "claim", "congratulations"
]

def predict_email(message):

    vector = vectorizer.transform([message])

    prediction = model.predict(vector)[0]

    probabilities = model.predict_proba(vector)[0]

    confidence = max(probabilities) * 100

    found_keywords = [
        word for word in spam_keywords
        if word.lower() in message.lower()
    ]

    return {
        "prediction": prediction,
        "confidence": round(confidence, 2),
        "keywords": found_keywords
    }