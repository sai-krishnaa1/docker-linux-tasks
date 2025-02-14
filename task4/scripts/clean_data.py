import pandas as pd
import os
import logging
 
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
 
def clean_data(data_path):
    merged_path = os.path.join(data_path, 'merged.csv')
    cleaned_path = os.path.join(data_path, 'cleaned.csv')
 
    if not os.path.exists(merged_path):
        logger.error(f"File {merged_path} not found. Ensure merging is done first.")
        return
 
    try:
        df = pd.read_csv(merged_path)
 
        # Handle missing values
        df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
        df['Age'].fillna(df['Age'].median(), inplace=True)  # Replace missing ages with median
        df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)  # Replace missing embarked with mode
 
        # Convert data types
        df['Embarked'] = df['Embarked'].astype('category')
 
        # Drop unnecessary columns
        df.drop(columns=['Cabin', 'Name', 'Ticket'], inplace=True, errors='ignore')
 
        # Save cleaned data
        df.to_csv(cleaned_path, index=False)
        logger.info(f"Cleaned data saved at {cleaned_path}")
 
    except Exception as e:
        logger.error(f"Error in clean_data: {e}")