import pandas as pd
import os
import logging
 
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
 
def transform_data(data_path):
    train_path = os.path.join(data_path, 'final_train.csv')
    test_path = os.path.join(data_path, 'final_test.csv')
    transformed_train_path = os.path.join(data_path, 'transformed_train.csv')
    transformed_test_path = os.path.join(data_path, 'transformed_test.csv')
 
    if not os.path.exists(train_path) or not os.path.exists(test_path):
        logger.error(f"Train/Test files not found in {data_path}. Ensure splitting is done first.")
        return
 
    try:
        train = pd.read_csv(train_path)
        test = pd.read_csv(test_path)
 
        # Apply One-Hot Encoding
        train = pd.get_dummies(train, columns=['Sex', 'Embarked'])
        test = pd.get_dummies(test, columns=['Sex', 'Embarked'])
 
        # Ensure train & test have same columns (if missing, add with default 0)
        for col in train.columns:
            if col not in test.columns:
                test[col] = 0
        for col in test.columns:
            if col not in train.columns:
                train[col] = 0
 
        # Align columns
        train = train.reindex(sorted(train.columns), axis=1)
        test = test.reindex(sorted(test.columns), axis=1)
 
        # Save transformed data
        train.to_csv(transformed_train_path, index=False)
        test.to_csv(transformed_test_path, index=False)
 
        logger.info(f"Transformed data saved successfully at {transformed_train_path} and {transformed_test_path}")
 
    except Exception as e:
        logger.error(f"Error in transform_data: {e}")