import pandas as pd
import os
import logging
from sklearn.model_selection import train_test_split
 
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
 
def split_data(data_path):
    cleaned_path = os.path.join(data_path, 'cleaned.csv')
    train_path = os.path.join(data_path, 'final_train.csv')
    test_path = os.path.join(data_path, 'final_test.csv')
 
    if not os.path.exists(cleaned_path):
        logger.error(f"File {cleaned_path} not found. Ensure cleaning is done first.")
        return
 
    try:
        df = pd.read_csv(cleaned_path)
 
        # Ensure there is enough data to split
        if df.shape[0] < 2:
            logger.error("Not enough data to perform train-test split.")
            return
 
        train, test = train_test_split(df, test_size=0.2, random_state=42)
 
        train.to_csv(train_path, index=False)
        test.to_csv(test_path, index=False)
 
        logger.info(f"Train/Test split completed: {train_path}, {test_path}")
 
    except Exception as e:
        logger.error(f"Error in split_data: {e}")