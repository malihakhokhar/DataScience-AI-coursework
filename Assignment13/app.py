from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model and features
model = joblib.load("churn_model.pkl")
features = joblib.load("features.pkl")

@app.route("/")
def home():
    return "Customer Churn Prediction API is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    input_df = pd.DataFrame([data])

    # Align input with training features
    input_df = input_df.reindex(columns=features, fill_value=0)

    prediction = model.predict(input_df)[0]

    return jsonify({
        "churn_prediction": int(prediction)
    })

if __name__ == "__main__":
    app.run(debug=True)

