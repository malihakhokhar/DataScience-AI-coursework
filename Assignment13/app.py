from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and feature names
model = joblib.load("churn_model.pkl")
features = joblib.load("features.pkl")

@app.route("/")
def home():
    return "Customer Churn Prediction Model is Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    input_data = pd.DataFrame([data])

    # Ensure correct feature order
    input_data = input_data.reindex(columns=features, fill_value=0)

    prediction = model.predict(input_data)[0]

    return jsonify({
        "churn_prediction": int(prediction)
    })

if __name__ == "__main__":
    app.run(debug=True)
