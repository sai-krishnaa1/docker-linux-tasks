import os
import pandas as pd
from src.batch.pipeline import main

def test_batch_prediction():
    # Ensure the batch data CSV exists
    batch_data_path = 'data/input/batch_data.csv'
    assert os.path.exists(batch_data_path), f"{batch_data_path} not found"

    # Run the batch pipeline (this will load the model, make predictions, and save the results)
    main()

    # Check if the predictions file was created
    predictions_file = 'data/output/batch_predictions.csv'
    assert os.path.exists(predictions_file), f"Predictions file not created: {predictions_file}"

    # Load and check the predictions CSV
    predictions_df = pd.read_csv(predictions_file)
    assert 'predictions' in predictions_df.columns, "Predictions column not found in the output CSV"
    assert len(predictions_df) > 0, "The predictions file is empty"
