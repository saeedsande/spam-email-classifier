from flask import Flask, render_template, request
from spam_classifier import predict_email

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    email_text = request.form["email"]

    result = predict_email(email_text)

    return render_template(
        "index.html",
        prediction=result["prediction"],
        confidence=result["confidence"],
        keywords=result["keywords"]
    )

if __name__ == "__main__":
    app.run(debug=True)