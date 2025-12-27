# Customer Churn Prediction – AI in Data Science

## 📌 Project Overview
This project implements an AI-based **Customer Churn Prediction system** that identifies customers who are likely to discontinue a service.  
It demonstrates a complete Data Science workflow including data preprocessing, model training, evaluation, deployment on localhost, and explainability.

The system is designed to support data-driven retention strategies in industries like telecommunications, banking, SaaS, and e-commerce.

---

## 🎯 Problem Statement
Customer churn directly impacts revenue and growth in competitive industries.  
Traditional analysis methods fail to detect churn early and do not scale with large datasets.

This project addresses the problem by using machine learning to predict churn and support proactive retention actions.

---

## 🧠 AI & Data Science Approach
The project follows an industry-standard pipeline:

1. Data loading and preprocessing  
2. Feature encoding and selection  
3. Machine learning model training (Random Forest Classifier)  
4. Model evaluation  
5. Model serialization (`churn_model.pkl` + `features.pkl`)  
6. Local deployment using Flask  
7. Explainability analysis (feature importance)

---

## 🏭 Industry Applications
This system can be applied in:

- Telecommunications (customer retention campaigns)  
- Banking and financial services  
- SaaS and subscription-based platforms  
- E-commerce platforms

---

## 🚀 Model Deployment (Localhost)
The trained model is deployed on **localhost** using the Flask web framework.  
The REST API accepts customer data and returns real-time churn predictions.

**API Endpoints:**

### Home
GET /

makefile
Copy code
Response:
Customer Churn Prediction API is running

shell
Copy code

### Predict Churn
POST /predict

pgsql
Copy code

**Sample JSON Input:**
```json
{
  "tenure": 5,
  "MonthlyCharges": 80,
  "TotalCharges": 400
}
Sample JSON Output:

json
Copy code
{
  "churn_prediction": 1
}
1 → Customer likely to churn

0 → Customer likely to stay

🔍 Explainability of the Model
The customer churn prediction model maps customer attributes (X) to churn outcomes (Y). Explainability ensures transparency and trust in the predictions.

A Random Forest classifier was used, which provides feature importance scores to identify which customer attributes most influence predictions. Analysis revealed that features such as tenure, monthly charges, and total charges have the strongest impact on churn decisions.

For example:

Customers with shorter tenure and high monthly charges are more likely to churn.

This explainability allows stakeholders to understand why a customer is predicted to churn and enables informed business decisions, such as targeted retention strategies. It ensures the model is not a black box and aligns with ethical AI principles.

📊 Model Evaluation Metrics
The model is evaluated using:

Accuracy

Precision

Recall

F1-Score

These metrics ensure the model reliably predicts churn while balancing false positives and false negatives.

🛠️ Tools & Technologies
Python

Anaconda

VS Code

Scikit-learn

Flask

Pandas & NumPy

📁 Project Structure
Copy code
Assignment13/
│
├── customer_churn.csv
├── train_model.py
├── app.py
├── explain_model.py
├── churn_model.pkl
├── features.pkl
├── README.md
⚖️ Ethical Considerations
Customer data privacy is maintained

Sensitive attributes are excluded

Predictions are used for decision support, not discrimination

The project aligns with responsible AI principles.

🔮 Future Enhancements
Web-based user interface

Real-time churn monitoring

Advanced deep learning models

Integration with CRM systems

✍️ Author
Maliha Khokhar
BS Software Engineering
AI in Data Science – Coursework

yaml
Copy code
