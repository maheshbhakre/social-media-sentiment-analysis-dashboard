# 📊 Social Media Sentiment Analysis Dashboard using Machine Learning & NLP

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data--Analysis-green)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![NLP](https://img.shields.io/badge/NLP-Sentiment--Analysis-purple)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Overview

This project implements an **end-to-end Social Media Sentiment Analysis Dashboard** using Machine Learning and Natural Language Processing (NLP) techniques to classify social media comments into:

- 😀 Positive
- 😡 Negative
- 😐 Neutral

The system analyzes text-based social media comments, predicts sentiment using Machine Learning models, and visualizes results through an interactive Streamlit dashboard.

---

# 🚀 Dashboard Preview

## 🔹 Dashboard Home

![Dashboard](./images/dash5.1.png)

---

## 🔹 Sentiment Prediction

![Dashboard](./images/dash5.2.png)

---

## 🔹 Visualization & Analytics

![Dashboard](./images/dash5.3.png)

---

## 🛠 Problem Statement

Companies receive thousands of customer comments, reviews, tweets, and feedback daily.

Manual analysis becomes difficult because:

- ❌ Huge volume of text data
- ❌ Real-time monitoring is difficult manually
- ❌ Negative comments may be missed
- ❌ Brand reputation changes rapidly
- ❌ Marketing response analysis is slow

---

## ✅ Solution

This project provides:

- 📊 Automated sentiment classification
- 🧠 NLP-based text preprocessing
- ⚡ Real-time sentiment prediction
- 📈 Sentiment visualization dashboard
- 🖥 Interactive Streamlit interface
- 🔍 CSV upload for bulk predictions
- 📉 Business insight generation

---

# 🏭 Industry Relevance

| Industry | Application |
|----------|-------------|
| E-Commerce | Product review analysis |
| Banking | Customer feedback monitoring |
| Food Delivery | Complaint analysis |
| Entertainment | Audience reaction analysis |
| Marketing | Campaign sentiment tracking |
| Politics | Public opinion analysis |
| Startups | Brand reputation monitoring |

---

# 📊 Business Impact

- 💬 Understand customer emotions instantly
- 📉 Detect negative feedback quickly
- 📈 Improve marketing strategies
- 🔒 Monitor brand reputation
- ⚡ Reduce manual analysis workload
- 📊 Generate actionable business insights

---

# ⚙ Tech Stack

- **Language:** Python
- **Data Processing:** Pandas, NumPy
- **NLP:** NLTK
- **Machine Learning:** Scikit-learn
- **Model:** Logistic Regression
- **Feature Extraction:** TF-IDF Vectorizer
- **Visualization:** Plotly, Matplotlib
- **Dashboard:** Streamlit
- **Model Storage:** Joblib

---

# 📊 Dataset

### Dataset Information

- Synthetic social media comments dataset
- Positive, Negative, and Neutral sentiments
- CSV-based structured dataset

### Features

- Text Comment
- Sentiment Label

### Target Classes

- `positive`
- `negative`
- `neutral`

---

# 🏗 System Architecture

```text
Social Media Comments
        ↓
Text Cleaning
        ↓
NLP Preprocessing
        ↓
TF-IDF Vectorization
        ↓
Machine Learning Model
        ↓
Sentiment Prediction
        ↓
Dashboard Visualization
```

---

# 📁 Project Structure

```text
Social-Media-Sentiment-Analysis-Dashboard/
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   ├── social_media_data.csv
│   └── cleaned_data.csv
│
├── images/
│   ├── dash5.1.png
│   ├── dash5.2.png
│   └── dash5.3.png
│
├── models/
│   ├── sentiment_model.pkl
│   └── vectorizer.pkl
│
├── src/
│   ├── data_preprocessing.py
│   ├── train_model.py
│   └── predict.py
│
├── requirements.txt
├── README.md
└── main.py
```

---

# ⚙ Installation & Setup

```bash
git clone https://github.com/maheshbhakre/social-media-sentiment-analysis-dashboard.git

cd social-media-sentiment-analysis-dashboard

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

# ▶️ Usage

## Run Data Preprocessing

```bash
python src/data_preprocessing.py
```

## Train Machine Learning Model

```bash
python src/train_model.py
```

## Run Streamlit Dashboard

```bash
streamlit run app/streamlit_app.py
```

---

# 📊 Model Performance

- ✅ Logistic Regression achieved strong sentiment classification accuracy
- ✅ TF-IDF improved text feature extraction
- ✅ Effective for NLP-based text classification tasks

### Evaluation Metrics Used

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

# 📸 PHASE-WISE IMPLEMENTATION

## 🔹 Phase 1 — Text Input & Prediction

![Phase1](./images/dash5.1.png)

---

## 🔹 Phase 2 — Sentiment Dashboard

![Phase2](./images/dash5.2.png)

---

## 🔹 Phase 3 — Visualization & Analytics

![Phase3](./images/dash5.3.png)

---

# 🧠 NLP + Machine Learning Workflow

```text
Social Media Comments
        ↓
Text Preprocessing
        ↓
TF-IDF Feature Extraction
        ↓
Machine Learning Model
        ↓
Sentiment Prediction
        ↓
Dashboard Visualization
```

---

# 🌍 Real-World Applications

- 🛒 Product Review Analysis
- 🍔 Food Delivery Feedback Monitoring
- 🎬 Movie & Entertainment Sentiment Analysis
- 🏦 Banking Customer Feedback
- 📱 Social Media Monitoring
- 📈 Marketing Campaign Analysis
- 🗳 Political Opinion Mining

---

# 🔥 Future Improvements

- BERT-based NLP Models
- Real-Time Twitter API Integration
- Emotion Detection
- Topic Modeling
- Multilingual Sentiment Analysis
- Cloud Deployment
- Live Streaming Dashboard

---

# 👨‍💻 Author

## Mahesh Bhakre

---

# 🌐 Connect With Me

<a href="https://github.com/maheshbhakre">
<img src="https://img.shields.io/badge/GitHub-Profile-black?style=for-the-badge&logo=github">
</a>

<a href="https://www.linkedin.com/in/maheshbhakreds1242">
<img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin">
</a>

<a href="https://www.instagram.com/mahesh_bhakre__2k06">
<img src="https://img.shields.io/badge/Instagram-Follow-purple?style=for-the-badge&logo=instagram">
</a>

<a href="https://saimfsd.github.io/mahesh-portfolio/">
<img src="https://img.shields.io/badge/Portfolio-Visit%20Website-orange?style=for-the-badge&logo=google-chrome">
</a>

---

# ⭐ NOTE

This project demonstrates a complete **end-to-end NLP and Machine Learning pipeline for Social Media Sentiment Analysis**, including:

- Text preprocessing
- NLP feature extraction
- TF-IDF vectorization
- Sentiment classification
- Model training
- Evaluation metrics
- Visualization dashboard
- Real-time prediction simulation

The project simulates how modern companies analyze customer emotions, public opinions, and brand reputation using Machine Learning and Natural Language Processing.

---

# 📜 License

This project is licensed under the MIT License.