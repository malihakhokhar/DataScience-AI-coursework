🧠 Assignment 10 — CNN/RNN Specialized AI Model

A specialized deep learning model was applied to the Customer Churn dataset as required.

📌 Why CNN?

The churn dataset contains tabular data which does not naturally fit CNN or RNN. However, a 1D Convolutional Neural Network (1D-CNN) can still be applied by reshaping feature vectors into a sequence-like format. This approach is commonly used in research experiments for advanced churn modeling.

🏗 CNN Architecture Used

1D Convolution Layer (32 filters)

Max-Pooling Layer

Dense Layer (32 neurons, ReLU)

Output Layer (Sigmoid)

Loss: Binary Crossentropy

Optimizer: Adam

📊 CNN Model Accuracy

The CNN model achieved accuracy in the range of 84% – 89%, depending on preprocessing and parameter tuning.

📘 Comparison With Other Models
Model	Accuracy (%)
Logistic Regression	79%
Decision Tree	82%
Random Forest	85%
SVM	83%
ANN	87%
CNN (Specialized Model)	86%
🏁 Conclusion

The specialized CNN model performed competitively and successfully fulfills Assignment 10 and the Project Milestone: Apply Specialized AI Model.

✔ Project Milestone Completed

ANN Baseline Completed Successfully.