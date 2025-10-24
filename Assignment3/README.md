# 🧠 Customer Churn Prediction — Data Visualization Report

## 📌 Objective
This project visualizes customer churn data to identify key factors that influence customer retention and churn behavior.

---

## 📂 Dataset
The dataset used is **customer_churn_dataset-testing-master.csv** (from Kaggle).  
It contains 11 columns including customer demographics, contract details, and churn status.

| Column | Description |
|---------|-------------|
| CustomerID | Unique ID for each customer |
| Age | Customer’s age |
| Gender | Male/Female |
| Tenure | Duration (in months) the customer has stayed |
| Usage Frequency | Average usage level |
| Payment Delay | Delay in payments |
| Subscription Type | Type of service subscribed |
| Contract Length | Duration of customer’s contract |
| Total Spend | Total spending of the customer |
| Last Interaction | Time since last contact |
| Churn | Whether the customer left (Yes/No) |

---

## 🧹 Data Cleaning Summary
- Removed duplicates  
- Handled missing values  
- Converted numerical columns to correct data types  
- Standardized categorical data (Yes/No, Male/Female)  

---

## 📊 Data Visualizations & Insights

### 1️⃣ Churn Distribution
Shows how many customers churned vs stayed.  
**Insight:** Majority didn’t churn, but a notable portion still left — retention strategies are needed.

### 2️⃣ Churn by Gender
Visualizes churn split by gender.  
**Insight:** Gender doesn’t significantly impact churn likelihood.

### 3️⃣ Churn by Contract Length
Displays churn rates across contract lengths.  
**Insight:** Shorter contracts see higher churn — long-term plans improve retention.

### 4️⃣ Total Spend vs Churn
Compares spending between churned and retained customers.  
**Insight:** Customers who spend less are more likely to churn — possibly due to lower satisfaction or engagement.

### 5️⃣ Tenure vs Churn
Shows tenure distribution among churned and loyal customers.  
**Insight:** Longer-tenure customers are more loyal, indicating that early retention efforts are critical.

---

## 🧩 Libraries Used
- **pandas**
- **matplotlib**
- **seaborn**

---

## 👩‍💻 Author
**Maliha Khokhar**  
BS Software Engineering | Customer Churn Prediction Project (Visualization Phase)