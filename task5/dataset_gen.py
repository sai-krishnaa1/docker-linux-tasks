import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()

# Create a DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Save it as CSV
df.to_csv('data/input/training_data.csv', index=False)

print("Iris dataset saved to 'data/input/training_data.csv'")
