import joblib
import os

# Define model path
MODEL_DIR = "src/model/artifacts"
MODEL_PATH = os.path.join(MODEL_DIR, "model.joblib")

def load_model():
    """Load the trained model."""
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
        print("Model loaded successfully!")
        return model
    else:
        print(f"Error: Model not found at {MODEL_PATH}")
        return None
