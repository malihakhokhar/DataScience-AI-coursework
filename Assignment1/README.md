# 🧠 AI & Data Science - Assignment 1

## 📘 Overview
This assignment focuses on loading, exploring, and analyzing a sample dataset using Python.  
The chosen dataset for this assignment is the **Titanic Dataset**. The main goal is to understand basic data handling and visualization in AI & Data Science using Python libraries.

---

## 🎯 Objectives
- Learn how to load and explore a dataset using Python (Pandas).
- Understand the structure and features of the Titanic dataset.
- Display the first few rows and basic statistics of the dataset.
- Prepare the foundation for further data analysis and machine learning tasks.

---

## 📂 Dataset
- **Name:** Titanic-Dataset.csv  
- **Source:** [Kaggle - Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic)  
- **Description:** The Titanic dataset contains information about passengers aboard the Titanic, including details like age, gender, passenger class, and survival status.

---

## 🧩 Technologies Used
- **Language:** Python  
- **Libraries:**  
  - `pandas` – for data loading and exploration  
  - `numpy` – for numerical computations  
  - `matplotlib` / `seaborn` (optional) – for visualization  

---

## 💻 Code Example

```python
import pandas as pd

# Load dataset
titanic_df = pd.read_csv("Titanic-Dataset.csv")

# Display first 10 rows
print("First 10 rows of the Titanic dataset:")
print(titanic_df.head(10))

# Basic information about dataset
print("\nDataset Info:")
print(titanic_df.info())

# Statistical summary
print("\nSummary Statistics:")
print(titanic_df.describe())
📊 Output Preview
The output displays the first 10 rows of the Titanic dataset along with basic information such as:

Column names

Data types

Non-null values

Basic statistics (mean, count, min, max, etc.)

✅ Conclusion
In this assignment, we successfully:

Imported and explored the Titanic dataset using Pandas.

Displayed the top rows of the dataset.

Understood the structure and type of data available for analysis.

This serves as the foundation for upcoming assignments involving data preprocessing, visualization, and machine learning.

✍️ Author

Name: Maliha Khokhar
Course: Artificial Intelligence & Data Science
Instructor: Dr.Mohsin Nazir
Semester: 7th 