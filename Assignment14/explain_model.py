import joblib
import pandas as pd

# Load model and features
model = joblib.load("churn_model.pkl")
features = joblib.load("features.pkl")

# Get feature importance
importance = model.feature_importances_

# Create DataFrame
importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": importance
}).sort_values(by="Importance", ascending=False)

print("Top factors influencing churn prediction:\n")
print(importance_df.head(10))
