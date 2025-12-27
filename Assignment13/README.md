# Customer Churn Prediction – AI in Data Science

## 📌 Project Overview
This project implements an AI-based **Customer Churn Prediction system** that identifies customers who are likely to discontinue a service. The system uses machine learning techniques to analyze historical customer data and is deployed locally using Flask.

The project demonstrates a complete Data Science workflow including data preprocessing, model training, evaluation, and **model deployment on localhost**.

---

## 🎯 Problem Statement
Customer churn directly impacts revenue and growth in competitive industries such as telecommunications, banking, and subscription-based services. Traditional analysis methods fail to detect churn early and do not scale well with large datasets.

This project addresses the problem by using machine learning models to predict churn and support proactive retention strategies.

---

## 🧠 AI & Data Science Approach
The project follows an industry-standard pipeline:

1. Data loading and preprocessing  
2. Feature encoding and selection  
3. Machine learning model training  
4. Model evaluation  
5. Model serialization  
6. Local deployment using Flask  

A Random Forest classifier is used to learn churn patterns from customer data.

---

## 🏭 Industry Applications
This churn prediction system can be applied in:

- Telecommunications (customer retention strategies)
- Banking and financial services
- SaaS and subscription-based platforms
- E-commerce platforms

---

## 🚀 Model Deployment (Localhost)
The trained model is deployed on **localhost** using the Flask web framework.  
The deployment exposes a REST API that accepts customer data and returns churn predictions in real time.

### Deployment Features
- Model loaded from serialized `.pkl` file  
- REST API for prediction requests  
- JSON-based input and output  
- Runs locally via VS Code and Anaconda  

---

## 📊 API Endpoints

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
├── churn_model.pkl
├── features.pkl
├── README.md
⚖️ Ethical Considerations
Customer data privacy is maintained

Sensitive personal attributes are excluded

Model predictions are used for decision support, not discrimination

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

markdown
Copy code

---

### Final blunt check
- ✔ Training covered  
- ✔ Deployment covered  
- ✔ Industry relevance clear  
- ✔ No fake claims  
