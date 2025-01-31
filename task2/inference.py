import joblib
import pandas as pd
import sys

# Load Logistic Regression model
model = joblib.load("/app/pima_model.pkl")

# Read input data
data = pd.read_csv("/app/diabetes.csv")

# Make predictions
predictions = model.predict(data.iloc[:, :-1])

# Save predictions
output_df = pd.DataFrame({"Predicted_Outcome": predictions})
output_df.to_csv("/app/data/predictions.csv", index=False)
