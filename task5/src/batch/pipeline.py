import sys
import os
import pandas as pd

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Ensure the output directory exists
output_dir = 'data/output'
os.makedirs(output_dir, exist_ok=True)

from src.model.model_loader import load_model

def main():
    # Load the trained model
    model = load_model()
    if model is None:
        print("Model not found. Exiting.")
        return

    # Read the batch data (e.g., from CSV)
    try:
        batch_data = pd.read_csv('data/input/batch_data.csv')
        print("Batch data loaded successfully!")
    except Exception as e:
        print(f"Error loading batch data: {e}")
        return

    # Ensure the batch data has the same columns as the training data (exclude 'target')
    input_features = batch_data.drop(columns=['target'], errors='ignore')  # Avoid error if no 'target'

    # Make predictions
    predictions = model.predict(input_features)

    # Add predictions to the batch data (optional)
    batch_data['predictions'] = predictions

    # Save the predictions to a new CSV file
    batch_data.to_csv(f'{output_dir}/batch_predictions.csv', index=False)
    print(f"Batch predictions saved to '{output_dir}/batch_predictions.csv'")

if __name__ == '__main__':
    main()
