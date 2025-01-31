import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
 
# Load dataset
data = pd.read_csv("diabetes.csv")
X = data.iloc[:, :-1]  # Features
y = data.iloc[:, -1]   # Target
 
# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 
# Train Logistic Regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
 
# Evaluate
preds = model.predict(X_test)
accuracy = accuracy_score(y_test, preds)
print(f"Model Accuracy: {accuracy:.4f}")
 
# Save model
joblib.dump(model, "pima_model.pkl")
print("Model saved as pima_model.pkl")
