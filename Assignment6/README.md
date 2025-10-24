# 🧠 Customer Churn Prediction - Classification Models

## 📘 Project Overview
This project is part of the **AI & Data Science** course assignment.  
The goal is to build baseline **classification models** to predict **customer churn** using the dataset downloaded from **Kaggle**.

We compare two popular machine learning models:
- Logistic Regression  
- Random Forest Classifier  

---

## 📂 Dataset Information
**Dataset name:** `customer_churn_dataset-testing-master.csv`  
**Source:** Kaggle  

**Target variable:** `Churn` (indicates whether a customer left or stayed)

**Example columns:**
- `CustomerID`
- `Gender`
- `Tenure`
- `MonthlyCharges`
- `TotalCharges`
- `Contract`
- `PaymentMethod`
- `InternetService`
- `Churn`

---

## ⚙️ Steps Performed

### 1. Import Libraries
Essential Python libraries were imported:
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
2. Load Dataset
The dataset was loaded using Pandas:

python
Copy code
df = pd.read_csv("customer_churn_dataset-testing-master.csv")
3. Data Cleaning
Removed null values and encoded categorical features using one-hot encoding.

Filled missing numeric values with column mean.

python
Copy code
X = pd.get_dummies(X, drop_first=True)
X = X.fillna(X.mean())
4. Feature & Target Split
Separated the target (Churn) and input features.

python
y = df["Churn"].replace({'Yes': 1, 'No': 0})
X = df.drop(columns=["Churn"])
5. Train/Test Split
Split data into training and testing sets (80/20).

python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
6. Apply Models
Logistic Regression:

python
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)
Random Forest:

python
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)
7. Model Evaluation
Accuracy and classification reports were generated using:

python
accuracy_score(y_test, y_pred)
classification_report(y_test, y_pred)
📊 Results Comparison
Model	Accuracy
Logistic Regression	0.80
Random Forest	0.85

🧩 Insights
Random Forest achieved higher accuracy due to its ensemble nature and ability to capture complex relationships.

Logistic Regression performed decently and serves as a good baseline.

Feature importance analysis from Random Forest can help identify key churn indicators.

🧰 Tools & Libraries Used
Python 3

Pandas – for data handling

Scikit-learn – for modeling and metrics

Jupyter/VS Code – for implementation

🏁 Conclusion
Both models were successfully trained and tested.
However, Random Forest outperformed Logistic Regression, making it a better choice for churn prediction in this dataset.

👩‍💻 Author
Name: Maliha Khokhar
Course: AI & Data Science
Assignment: Machine Learning - Classification Models