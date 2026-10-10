# 🛒 FreshCart 360 — Customer Support Ticket Classifier

FreshCart 360 is a machine learning project that classifies customer support tickets and predicts urgency levels using Natural Language Processing (NLP).

## ✨ Features
- Predicts customer ticket categories.
- Classifies urgency as High, Medium, or Low.
- Provides a simple interactive Streamlit interface.
- Includes a sidebar with application information and usage instructions.

## 🛠️ Technologies
- Python
- Pandas
- Scikit-learn
- TF-IDF
- Logistic Regression
- Streamlit
- Joblib

## 📂 Project Structure
```text
FreshCart360/
├── app.py
├── requirements.txt
├── freshcart_category_model.joblib
└── freshcart_urgency_model.joblib
```

## 🚀 Getting Started

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the application
```bash
streamlit run app.py
```

Make sure both saved model files are available in the same directory as `app.py`.

## 💡 How to Use
1. Enter a customer's support message.
2. Click **Predict Ticket**.
3. Review the predicted category and urgency.

## ⚠️ Limitations
This is a baseline prototype. The initial dataset uses rule-generated labels, so predictions require further validation using human-labeled data before real-world deployment.

## 🎯 Project Goal
To help customer support teams organize incoming tickets and identify urgent complaints more efficiently.
