import pandas as pd
import os
import logging
 
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
 
def merge_data(data_path):
    train_path = os.path.join(data_path, 'train.csv')
    test_path = os.path.join(data_path, 'test.csv')
    merged_path = os.path.join(data_path, 'merged.csv')
 
    if not os.path.exists(train_path) or not os.path.exists(test_path):
        logger.error(f"Missing files. Ensure 'train.csv' and 'test.csv' exist in {data_path}.")
        return
 
    try:
        train = pd.read_csv(train_path)
        test = pd.read_csv(test_path)
 
        train['train_test'] = 'train'
        test['train_test'] = 'test'
 
        merged = pd.concat([train, test], ignore_index=True)
        merged.to_csv(merged_path, index=False)
 
        logger.info(f"Merged data saved at {merged_path}")
    except Exception as e:
        logger.error(f"Error in merge_data: {e}")