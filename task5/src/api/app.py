from flask import Flask, request, jsonify, render_template
from model.model_loader import load_model
import numpy as np
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

# Define required features globally
REQUIRED_FEATURES = [
    "sepal length (cm)",
    "sepal width (cm)", 
    "petal length (cm)",
    "petal width (cm)"
]

# Load the model when the app starts
try:
    model = load_model()
    logging.info("Model loaded successfully")
except Exception as e:
    model = None
    logging.error(f"Error loading model: {e}")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    logging.debug(f"Received request data: {request.get_json()}")
    
    try:
        # Get and validate input data exists
        data = request.get_json()
        if data is None:  # Check if None specifically
            logging.warning("No JSON data received")
            return jsonify({"error": "No input data provided"}), 400
            
        if len(data) == 0:  # Check if empty dict
            logging.warning("Empty JSON object received")
            return jsonify({"error": "No input data provided"}), 400

        # Check for missing features
        missing_features = [feat for feat in REQUIRED_FEATURES if feat not in data]
        if missing_features:
            logging.warning(f"Missing features: {missing_features}")
            return jsonify({
                "error": "Missing required features",
                "missing_features": missing_features
            }), 400

        # Validate feature values
        try:
            features = np.array([float(data[feat]) for feat in REQUIRED_FEATURES]).reshape(1, -1)
        except (ValueError, TypeError) as e:
            logging.warning(f"Invalid feature values: {e}")
            return jsonify({
                "error": "Invalid feature values. All features must be numeric."
            }), 400

        # Make prediction
        if model is None:
            logging.error("Model not loaded")
            return jsonify({"error": "Model not loaded"}), 500

        prediction = model.predict(features)
        logging.info(f"Successful prediction: {prediction[0]}")
        return jsonify({"prediction": int(prediction[0])}), 200

    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}", exc_info=True)
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)