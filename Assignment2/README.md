# 🧹 Data Cleaning Report — Customer Churn Prediction

## 📘 Overview
This report shows the process of cleaning the **Customer Churn Dataset** from Kaggle.  
Data cleaning is an essential step to prepare the dataset for accurate and efficient machine learning modeling.

---

## 📊 Before Cleaning

### Summary
- Dataset contained **missing values** in columns such as `TotalCharges` and some categorical fields.  
- There were a few **duplicate records**.  
- Data types were inconsistent — some numerical columns were stored as strings.  
- Null entries could affect model accuracy if not handled.

### Example (Before Cleaning)
| Column | Missing Values | Data Type | Example Issue |
|---------|----------------|------------|----------------|
| TotalCharges | 11 | object | Numeric values stored as text |
| SeniorCitizen | 0 | int64 | - |
| InternetService | 0 | object | - |

---

## 🧹 Cleaning Steps Applied

1. **Removed Duplicates**  
   - Used `drop_duplicates()` to remove redundant entries.

2. **Handled Missing Values**  
   - Filled missing numeric values with the **mean**.  
   - Filled missing categorical values with the **mode**.  
   - Converted text-based numeric columns (`TotalCharges`) to numeric format.

3. **Checked Data Types and Consistency**  
   - Ensured all numeric fields are in proper numerical format.  
   - Verified all categorical columns contain valid category names.

---

## 📈 After Cleaning

### Summary
| Column | Missing Values | Data Type | Cleaned? |
|---------|----------------|------------|-----------|
| TotalCharges | 0 | float64 | ✅ |
| SeniorCitizen | 0 | int64 | ✅ |
| InternetService | 0 | object | ✅ |

### Dataset Shape
| Stage | Rows | Columns |
|--------|-------|----------|
| Before Cleaning | 7043 | 21 |
| After Cleaning | 7043 | 21 |

---

## ✅ Conclusion
After cleaning:
- All missing and duplicate values were handled.
- Data types were corrected.
- The dataset is now ready for feature engineering and model training.

---

## ✍️ Author
**Name:** Maliha Khokhar  
**Project:** Customer Churn Prediction  
**Course:** AI & Data Science  
**Instructor:** Dr.Mohsin Nazir
**Semester:** 7th