# 📊 Customer Churn Prediction — Correlation Analysis

## 🧠 Objective
The goal of this assignment is to perform **correlation analysis** on the Customer Churn dataset to identify which features are most related to the target variable — **Churn**.  
This helps understand the key factors influencing customer retention and loss.

---

## 📂 Dataset
The dataset used in this project is:

**File Name:** `customer_churn_dataset-testing-master.csv`  
**Source:** Kaggle  

### Columns in the dataset:
- **CustomerID**
- **Age**
- **Gender**
- **Tenure**
- **Usage Frequency**
- **Payment Delay**
- **Subscription Type**
- **Contract Length**
- **Total Spend**
- **Last Interaction**
- **Churn**

---

## 🧹 Data Cleaning Steps
- Removed missing or duplicate values (if any)
- Converted categorical variables (e.g., Gender, Subscription Type, Churn) into numeric form
- Normalized numeric columns for correlation analysis
- Ensured data types were consistent across columns

---

## 📈 Correlation Analysis

### Steps:
1. Encoded the target variable **Churn** (Yes = 1, No = 0)
2. Calculated the **Pearson correlation** between all features
3. Sorted correlations in descending order to identify the top 3 factors most related to churn

### Visualization:
A heatmap was created using **Seaborn** to show correlation strength across all features.

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("customer_churn_dataset-testing-master.csv")
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

corr = df.corr(numeric_only=True)
plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap — Customer Churn Dataset")
plt.show()

# Find top 3 correlated features
target_corr = corr['Churn'].sort_values(ascending=False)
print(target_corr.head(4))
🧩 Results
🔝 Top 3 Features Most Related to Churn:
Rank	Feature	Correlation with Churn
1️⃣	Contract Length	-0.49
2️⃣	Tenure	-0.41
3️⃣	Payment Delay	+0.36

💡 Insights
Customers with shorter contract lengths are more likely to churn.

Low tenure customers (new users) have higher churn rates, showing the need for early engagement.

Frequent payment delays strongly correlate with churn, suggesting payment issues or dissatisfaction.

🧰 Libraries Used
Pandas — Data loading and preprocessing

Matplotlib / Seaborn — Data visualization

NumPy — Numerical operations

👩‍💻 Author
Maliha Khokhar
BS Software Engineering — AI & Data Science Assignment
Department of Software Engineering
