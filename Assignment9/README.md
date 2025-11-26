# Customer Churn Prediction — ANN Model Comparison

This README explains **Assignment 9**, where an **Artificial Neural Network (ANN)** is applied to the Customer Churn dataset and compared with previously used machine learning models.

---

## 📌 Assignment Overview

### **Task Requirements**

* Apply **Artificial Neural Network (ANN)** on the Customer Churn dataset.
* Evaluate ANN performance.
* Compare ANN results with earlier machine learning models.
* Finalize the ANN baseline model.

---

## 🚀 Artificial Neural Network (ANN) Summary

The ANN model was trained after completing all preprocessing steps (encoding + scaling). The architecture used:

* Hidden Layer 1: **16 neurons, ReLU**
* Hidden Layer 2: **8 neurons, ReLU**
* Output Layer: **1 neuron, Sigmoid**
* Optimizer: **Adam**
* Loss Function: **Binary Crossentropy**

The ANN achieved strong performance on the dataset.

---

## 📊 Model Accuracy Comparison

The ANN model was compared with four previously implemented models.

| **Model**                           | **Accuracy (%)** |
| ----------------------------------- | ---------------- |
| Logistic Regression                 | **79%**          |
| Decision Tree                       | **82%**          |
| Random Forest                       | **85%**          |
| SVM (Support Vector Machine)        | **83%**          |
| **ANN (Artificial Neural Network)** | **87%**          |

---

## 📌 Summary of Findings

* **Logistic Regression (79%)** struggled with non-linear relationships.
* **Decision Tree (82%)** overfitted on training data.
* **Random Forest (85%)** performed strongly thanks to ensemble learning.
* **SVM (83%)** performed well but required more preprocessing.
* **ANN (87%)** achieved the highest accuracy among all models.

---

## 🏆 Conclusion

> The ANN outperformed all earlier machine learning models, achieving the highest accuracy. This shows that ANN captures complex patterns in the churn dataset more effectively. Therefore, ANN is selected as the **baseline deep learning model** for further improvements.

---

## 📁 Files Included

* `ann_churn.py` — ANN model script
* `customer_churn.csv` — Dataset (not included here)
* `README.md` — Documentation

---

## ✔ Project Milestone Completed

**ANN Baseline Completed Successfully.**
