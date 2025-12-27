import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
data = pd.read_csv("customer_churn_dataset.csv")

# Basic preprocessing (adjust column names if needed)
X = data.drop("Churn", axis=1)
y = data["Churn"]

# Convert categorical columns if any
X = pd.get_dummies(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "churn_model.pkl")
joblib.dump(X.columns, "features.pkl")

print("Model trained and saved successfully.")
