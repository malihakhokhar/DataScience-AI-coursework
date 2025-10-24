# 🧠 Customer Churn Prediction – Regression Analysis

## 📘 Assignment Overview
This assignment focuses on applying **regression analysis** to the Customer Churn dataset obtained from Kaggle.  
The goal is to build a predictive model using **train/test split** and evaluate its performance using **Mean Absolute Error (MAE)** and **Root Mean Square Error (RMSE)**.

---

## 📊 Dataset Description
The dataset contains customer data with features such as:
- `gender`, `SeniorCitizen`, `Partner`, `Dependents`
- `tenure`, `MonthlyCharges`, `TotalCharges`
- `Contract`, `PaymentMethod`, `InternetService`, etc.
- **Target Variable:** `Churn` (Yes/No)

For regression analysis, categorical features were encoded numerically and the target variable was transformed into binary format (Yes = 1, No = 0).

---

## ⚙️ Steps Performed

### 1. Data Loading
The dataset was loaded using pandas:
```python
import pandas as pd
df = pd.read_csv("customer_churn_dataset-testing-master.csv")
2. Data Preprocessing
Handled missing values.

Encoded categorical columns using LabelEncoder and one-hot encoding.

Converted Churn column into binary (1 = Yes, 0 = No).

3. Train/Test Split
The dataset was divided into training and testing sets:

python
Copy code
from sklearn.model_selection import train_test_split

X = df.drop('Churn', axis=1)
y = df['Churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
4. Applying Regression
A Linear Regression model was trained:

python
Copy code
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
5. Model Evaluation
Predictions were compared using MAE and RMSE:

python
Copy code
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("Mean Absolute Error (MAE):", mae)
print("Root Mean Squared Error (RMSE):", rmse)
📈 Results
Metric	Description	Value
MAE	Average absolute difference between predicted and actual churn values.	(Add your result here)
RMSE	Penalizes larger errors more than MAE.	(Add your result here)

Interpretation:

Lower MAE and RMSE indicate a more accurate model.

The regression model provides insight into how numerical features (e.g., tenure, charges) relate to churn probability.

📦 Dependencies
Install all required libraries before running the notebook:

bash
Copy code
pip install pandas numpy scikit-learn matplotlib seaborn
📁 Files
customer_churn_dataset-testing-master.csv – Dataset file

churn_regression.ipynb – Jupyter notebook with full code

README.md – This documentation file

✨ Conclusion
This regression analysis demonstrates how customer attributes affect churn likelihood.
Although churn is a classification problem, regression helps to quantify the strength of relationships between customer features and churn probability.

Prepared by: Maliha Khokhar
Course: Artificial Intelligence & Data Science
Assignment: Regression Analysis on Customer Churn Dataset
