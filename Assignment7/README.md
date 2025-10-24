# 📊 Model Evaluation and Visualization — Customer Churn Prediction

This section presents the evaluation of two classification models — **Logistic Regression** and **Random Forest** — applied on the *Customer Churn Prediction* dataset.  
The models were evaluated using key metrics such as **Precision**, **Recall**, **F1-Score**, and **Accuracy** to understand their overall performance.

---

## 🧪 Models Used
- **Logistic Regression:** A baseline linear model used to predict churn probability based on customer attributes.  
- **Random Forest Classifier:** An ensemble model combining multiple decision trees to improve prediction accuracy and reduce overfitting.

---

## 📈 Evaluation Metrics Overview

| Metric | Description |
|:-------|:-------------|
| **Precision** | Measures how many of the predicted positive cases were actually positive. |
| **Recall** | Measures how many of the actual positive cases were correctly identified. |
| **F1-Score** | Harmonic mean of Precision and Recall — useful for imbalanced datasets. |
| **Accuracy** | Proportion of total correct predictions (both positive and negative). |

---

## 📊 1️⃣ Precision, Recall, and F1-Score Comparison

This bar chart visualizes the **Precision**, **Recall**, and **F1-Score** for both Logistic Regression and Random Forest.  
It helps identify how well each model performs across key classification metrics.

![Precision Recall F1 Bar Chart](precision_recall_f1_chart.png)

### 🔍 Insights:
- **Random Forest** outperformed **Logistic Regression** across all metrics.
- The difference is especially visible in **F1-score**, indicating better balance between precision and recall.
- Logistic Regression performed decently but lacked non-linear feature learning.

---

## 📊 2️⃣ Accuracy Comparison

This chart highlights the **overall accuracy** of both models.

![Accuracy Comparison Bar Chart](accuracy_comparison_chart.png)

### 🔍 Insights:
- **Random Forest achieved 100% accuracy**, indicating it captured data patterns exceptionally well.
- **Logistic Regression** achieved **~86% accuracy**, which is reasonable for a linear baseline model.
- For real-world deployment, additional validation (e.g., cross-validation or unseen test data) should ensure Random Forest’s high accuracy is not due to overfitting.

---

## 🎯 Final Evaluation Metric

After reviewing results, **F1-Score** is chosen as the **final evaluation metric** for the Customer Churn Prediction project.

### ✅ Reason:
- The dataset represents a **classification problem with potential class imbalance** (churn vs. non-churn).  
- **F1-Score** provides a balanced measure of **precision and recall**, making it ideal for evaluating performance in customer churn scenarios.  
- High F1 ensures the model effectively captures true churners without excessive false positives.

---

## 🧠 Summary
- **Best Performing Model:** Random Forest  
- **Key Metric Chosen:** F1-Score  
- **Rationale:** Provides a fair balance between identifying actual churners and minimizing false predictions.  

---

### 📁 Files
- `precision_recall_f1_chart.png` — Comparison of Precision, Recall, and F1-Score  
- `accuracy_comparison_chart.png` — Accuracy comparison between models  
- `evaluation_report.ipynb` — Jupyter notebook containing code for training, evaluation, and visualization  

---

### 👩‍💻 Author
**Maliha Khokhar**  
*AI & DS Assignment — Customer Churn Prediction Project*  
*Semester: BS Software Engineering*  