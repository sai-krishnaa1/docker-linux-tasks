import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Set the experiment name
mlflow.set_experiment('breast_cancer_experiment')
print("Experiment set: 'breast_cancer_experiment'")

# Load dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Standardize the data
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Function to perform hyperparameter search using GridSearchCV or RandomizedSearchCV
def perform_search(model, param_grid, search_type='grid', n_iter=10):
    if search_type == 'grid':
        search = GridSearchCV(model, param_grid, cv=5, n_jobs=-1, verbose=1)
    elif search_type == 'random':
        search = RandomizedSearchCV(model, param_grid, n_iter=n_iter, cv=5, n_jobs=-1, verbose=1)
    
    search.fit(X_train, y_train)
    return search.best_estimator_, search.best_params_, search.best_score_

# Define the models and their hyperparameter grids
models = {
    'RandomForest': RandomForestClassifier(),
    'SVM': SVC(),
    'LogisticRegression': LogisticRegression(max_iter=10000)
}

param_grids = {
    'RandomForest': {
        'n_estimators': [50, 100, 200],
        'max_depth': [3, 5, 10],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 5],
    },
    'SVM': {
        'C': [0.1, 1, 10],
        'kernel': ['linear', 'rbf'],
    },
    'LogisticRegression': {
        'C': [0.1, 1, 10],
        'solver': ['liblinear', 'saga'],
    }
}

# Function to run the experiment and log it to MLFlow
def run_experiment(model_name, model, param_grid, search_type='grid', use_random_search=False):
    # Start a new MLFlow run
    with mlflow.start_run():
        mlflow.log_param('model', model_name)
        mlflow.log_param('search_type', search_type)
        
        # Perform hyperparameter search
        search = 'random' if use_random_search else search_type
        best_model, best_params, best_score = perform_search(model, param_grid, search, n_iter=10)

        # Evaluate the model
        y_pred = best_model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        # Log the parameters, accuracy, and best model
        mlflow.log_params(best_params)
        mlflow.log_metric('accuracy', accuracy)
        
        # Log the best model
        mlflow.sklearn.log_model(best_model, "best_model")
        
        # Log artifacts (e.g., model pickle)
        artifact_dir = "./artifacts"
        os.makedirs(artifact_dir, exist_ok=True)
        model_path = os.path.join(artifact_dir, f"{model_name}_best_model.pkl")
        joblib.dump(best_model, model_path)
        mlflow.log_artifacts(artifact_dir)

        print(f"Best Model: {best_params}, Accuracy: {accuracy}")
        return best_model, best_params, accuracy

# Running experiments with different models and search types
for model_name, model in models.items():
    print(f"Running experiment with {model_name}...")
    best_model, best_params, accuracy = run_experiment(model_name, model, param_grids[model_name], search_type='grid', use_random_search=False)
    print(f"Experiment with {model_name} completed. Best accuracy: {accuracy}")
    
    # Running with random search
    print(f"Running experiment with {model_name} (Random Search)...")
    best_model, best_params, accuracy = run_experiment(model_name, model, param_grids[model_name], search_type='random', use_random_search=True)
    print(f"Random Search experiment with {model_name} completed. Best accuracy: {accuracy}")
