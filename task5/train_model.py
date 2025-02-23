import joblib
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Define model path
MODEL_DIR = "src/model/artifacts"
MODEL_PATH = os.path.join(MODEL_DIR, "model.joblib")

# Ensure artifacts directory exists
os.makedirs(MODEL_DIR, exist_ok=True)

# Load dataset from CSV
df = pd.read_csv('data/input/training_data.csv')

# Split into features (X) and target (y)
X = df.drop(columns=["target"])  # All columns except 'target'
y = df["target"]  # Target column

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Define model pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),  # Standardizing features
    ("model", LogisticRegression(max_iter=200))
])

# Train model
pipeline.fit(X_train, y_train)

# Evaluate model
accuracy = pipeline.score(X_test, y_test)
print(f"Model Accuracy: {accuracy:.4f}")

# Save model
joblib.dump(pipeline, MODEL_PATH)
print(f"Model saved at {MODEL_PATH}")
