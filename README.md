

# Customer Churn Prediction 🔍  
**End-to-End Data Science & AI Project**

---

## 📌 Overview

This project builds a **complete AI-driven Customer Churn Prediction system**, covering:

- Data preprocessing  
- Machine Learning & Deep Learning models  
- NLP preprocessing  
- Model explainability  
- REST API deployment  

Originally developed across **13 assignments**, it is consolidated here as a **single industry-style project**.

---

## 🎯 Problem Statement

Customer churn reduces revenue and growth in competitive industries.  
Traditional analytics fail to detect churn early or scale effectively.

This project predicts **which customers are likely to churn** and explains *why*.

---

## 🧠 Pipeline Summary

```

## Data → Preprocessing → ML / DL Models → Evaluation → Explainability → Deployment

````

---

## ⚙️ Techniques Used

### 🔹 Supervised Learning
- Linear Regression
- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine

### 🔹 Unsupervised Learning
- K-Means Clustering
- PCA (Dimensionality Reduction)

### 🔹 Deep Learning
- ANN (Baseline DL Model)
- 1D-CNN (Specialized Model)

### 🔹 NLP
- Tokenization
- Stopword Removal
- TF-IDF Vectorization

---

## 📊 Model Performance (Accuracy)

| Model | Accuracy |
|------|---------|
| Logistic Regression | 79% |
| Decision Tree | 82% |
| Random Forest | 85% |
| SVM | 83% |
| ANN | **87%** |
| CNN | ~86% |

✔ **ANN selected as best-performing model**

---

## 🚀 Deployment (Flask API)

**Endpoint**
```http
POST /predict
````

**Input**

```json
{
  "tenure": 5,
  "MonthlyCharges": 80,
  "TotalCharges": 400
}
```

**Output**

```json
{
  "churn_prediction": 1
}
```

* `1` → Likely to churn
* `0` → Likely to stay

Runs locally using **VS Code + Anaconda**.

---

## 🔍 Explainability

Random Forest feature importance revealed:

* **Tenure**
* **Monthly Charges**
* **Total Charges**

> Short tenure + high monthly cost = higher churn risk

This ensures transparency and ethical AI usage.

---

## 🏭 Industry Use Cases

* Telecommunications
* Banking & Finance
* SaaS & Subscriptions
* E-commerce

---

## 🛠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* TensorFlow / Keras
* Flask
* Matplotlib / Seaborn

---

## 📁 Project Structure

```
DS_AI_Project/
│
├── data/
├── notebooks/
├── models/
├── reports/
├── visuals/
│
├── app.py
├── train_model.py
├── explain_model.py
├── ann_churn.py
├── churn_model.pkl
├── features.pkl
└── README.md
```

---

## 🔮 Future Work

* Web UI (Streamlit / React)
* Real-time churn monitoring
* Advanced deep learning models
* CRM integration

---

## 👩‍💻 Author

**Maliha Khokhar**
BS Software Engineering
AI & Data Science Coursework

---

> This repository demonstrates practical skills in **Data Science, AI modeling, and deployment** — not just theory.

```

---

### Brutal truth (since you asked for it)
- Your **content was fine**
- Your **presentation was weak**
- This version fixes that

If you want:
- a **FYP-level README**
- a **resume-ready GitHub description**
- or **README + report alignment**

say it directly.
```
