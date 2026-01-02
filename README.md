🚀 Customer Churn Prediction — Data Science & AI Project

An end-to-end Data Science & Artificial Intelligence system for predicting customer churn using Machine Learning, Deep Learning, NLP, and Model Deployment.

This repository consolidates 13 academic assignments into a single coherent project, following industry-standard workflows and ethical AI principles.

📌 Project Summary

Customer churn prediction is a high-impact AI use case across industries such as telecommunications, banking, SaaS, and e-commerce.
This project builds a complete churn prediction pipeline:

Data preprocessing & validation

Supervised & unsupervised learning

Deep learning model comparison

NLP preprocessing

Model explainability

REST API deployment using Flask

The goal is not just prediction — but interpretable, deployable, and responsible AI.

🧠 Data Science Workflow
1️⃣ Data Preprocessing

Missing values handled using median (numeric) and mode (categorical)

Categorical encoding using Label Encoding

Feature scaling using StandardScaler

Train-test split: 80 / 20

Data consistency and validation checks applied

2️⃣ Regression Analysis

Objective: Predict continuous outcomes

Model: Linear Regression

Metrics:

MAE

MSE

R² Score

Visualization: Actual vs Predicted Scatter Plots

3️⃣ Classification Analysis

Objective: Predict churn (Yes / No)

Models

Logistic Regression

Random Forest Classifier

Evaluation Metrics

Accuracy

Precision

Recall

F1-Score

Key Decision:
F1-Score prioritized to balance false positives and false negatives.

4️⃣ Clustering Analysis

Objective: Discover hidden customer segments

Algorithm: K-Means

Optimal clusters identified using Elbow Method

Dimensionality reduction using PCA

2D cluster visualization for interpretability

🤖 Deep Learning Models
🔹 ANN — Assignment 9

Architecture

Dense (16 neurons, ReLU)

Dense (8 neurons, ReLU)

Output (Sigmoid)

Optimizer: Adam

Loss: Binary Crossentropy

Model Accuracy Comparison

Model	Accuracy
Logistic Regression	79%
Decision Tree	82%
Random Forest	85%
SVM	83%
ANN	87%

✔ ANN selected as baseline deep learning model.

🔹 CNN (Specialized Model) — Assignment 10

Applied 1D-CNN to tabular churn data (experimental setup)

Accuracy range: 84% – 89%

Demonstrates feasibility of specialized AI models beyond traditional ML

🧾 NLP Component — Assignment 11

To demonstrate NLP preprocessing:

Text normalization (lowercasing)

Tokenization

Stopword removal

TF-IDF vectorization

A dummy Customer_Feedback column was introduced to simulate real-world text data.

🚀 Model Deployment (Flask API)

The final churn model is deployed locally using Flask.

🔌 API Endpoints

Home

GET /


Response:

Customer Churn Prediction API is running


Predict Churn

POST /predict


Sample Input

{
  "tenure": 5,
  "MonthlyCharges": 80,
  "TotalCharges": 400
}


Sample Output

{
  "churn_prediction": 1
}


1 → Customer likely to churn

0 → Customer likely to stay

🔍 Model Explainability

A Random Forest Classifier was used for deployment to enable feature importance analysis.

Most influential features

Tenure

Monthly Charges

Total Charges

Insight Example

Customers with shorter tenure and higher monthly charges show a higher probability of churn.

This ensures transparency and supports ethical AI decision-making.

⚖️ Ethical AI Practices

Customer privacy preserved

Sensitive attributes excluded

Predictions used for decision support only

Model behavior is explainable and auditable

🏭 Industry Applications

Telecommunications (customer retention)

Banking & financial services

SaaS & subscription platforms

E-commerce businesses

🛠️ Tech Stack

Python

Pandas, NumPy

Scikit-learn

TensorFlow / Keras

Flask

Matplotlib / Seaborn

VS Code + Anaconda

📁 Repository Structure
DS_AI_Project/
│
├── data/
├── notebooks/
├── models/
├── visuals/
├── reports/
│
├── regression_analysis.ipynb
├── classification_analysis.ipynb
├── clustering_analysis.ipynb
├── ann_churn.py
├── train_model.py
├── explain_model.py
├── app.py
│
├── churn_model.pkl
├── features.pkl
└── README.md

🔮 Future Improvements

Web-based frontend (Streamlit / React)

Real-time churn monitoring

Advanced deep learning architectures

CRM system integration

👩‍💻 Author

Maliha Khokhar
BS Software Engineering
AI & Data Science Coursework
