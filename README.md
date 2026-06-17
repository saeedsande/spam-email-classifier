# 🛡️ AI Spam Email Classifier

A Machine Learning-powered web application that automatically detects whether an email/message is **Spam** or **Ham (Legitimate)** using Natural Language Processing (NLP) and text classification techniques.

## 🚀 Project Overview

Spam emails are one of the most common cybersecurity threats, often containing phishing attempts, fraudulent offers, and malicious links. This project uses Machine Learning to analyze email content and classify messages as either Spam or Legitimate.

The application provides:

* Real-time spam detection
* Confidence score prediction
* Suspicious keyword identification
* Interactive web dashboard
* Machine Learning-based classification

---

## ✨ Features

### 📧 Email Analysis

* Analyze email/message content instantly
* Classify messages as Spam or Ham

### 📊 Confidence Score

* Displays prediction confidence percentage
* Helps users understand model certainty

### 🔍 Suspicious Keyword Detection

* Highlights potentially dangerous terms such as:

  * Win
  * Free
  * Cash
  * Prize
  * Reward
  * Lottery
  * Claim

### 🖥️ Interactive Dashboard

* User-friendly web interface
* Responsive design
* Real-time prediction results

### 🤖 Machine Learning Model

* TF-IDF Vectorization
* Multinomial Naive Bayes Classifier
* Trained on the SMS Spam Collection Dataset

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-Learn
* TF-IDF Vectorizer
* Multinomial Naive Bayes

### Web Development

* Flask
* HTML5
* CSS3

### Data Processing

* Pandas
* Joblib

---

## 📂 Project Structure

```bash
spam-email-classifier/
│
├── app.py
├── train_model.py
├── spam_classifier.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
│
├── dataset/
│   └── spam.csv
│
├── templates/
│   └── index.html
│
├── screenshots/
│   ├── dashboard.png
│   └── prediction.png
│
└── static/
```

## 📊 Dataset

Dataset Used:

SMS Spam Collection Dataset

Dataset Statistics:

* Total Messages: 5,572
* Spam Messages: 747
* Legitimate Messages: 4,825

The dataset contains real SMS messages labeled as Spam or Ham.

---

## ⚙️ Machine Learning Workflow

1. Load Dataset
2. Data Cleaning & Preprocessing
3. TF-IDF Feature Extraction
4. Train-Test Split
5. Model Training (Multinomial Naive Bayes)
6. Accuracy Evaluation
7. Model Serialization using Joblib
8. Flask Web Application Deployment

---

## 🎯 Model Performance

| Metric        | Value                   |
| ------------- | ----------------------- |
| Algorithm     | Multinomial Naive Bayes |
| Vectorization | TF-IDF                  |
| Dataset Size  | 5,572 Messages          |
| Accuracy      | 96% - 98%               |

---

## 🧪 Example Predictions

### Example 1

Input:

Congratulations! You have won ₹50,000. Click here now to claim your prize.

Prediction:

SPAM

Confidence:

98%

---

### Example 2

Input:

Hi Saeed, Please attend tomorrow's project review meeting at 10 AM.

Prediction:

HAM

Confidence:

97%

---

## 🚀 Installation

Clone Repository

```bash
git clone https://github.com/yourusername/spam-email-classifier.git
```

Navigate to Project Directory

```bash
cd spam-email-classifier
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Train Model

```bash
python train_model.py
```

Run Application

```bash
python app.py
```

Open Browser

```bash
http://127.0.0.1:5000
```

---

## 📸 Screenshots

### Dashboard

Add Screenshot Here

### Prediction Result

Add Screenshot Here

---

## 🔮 Future Enhancements

* Deep Learning-based Classification
* Phishing URL Detection
* Email Attachment Analysis
* User Authentication
* Cloud Deployment
* Real-time Email Integration
* Multi-language Spam Detection

---

## 👨‍💻 Author

**Saeed Ismail Sande**

B.Tech Computer Science Engineering

Software Engineer | Full Stack & Mobile Application Developer

GitHub: https://github.com/saeedsande

LinkedIn: Add Your LinkedIn Profile Link

---

## ⭐ Support

If you found this project useful, consider giving it a star ⭐ on GitHub.
