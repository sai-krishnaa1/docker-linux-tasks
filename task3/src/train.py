import json
import os
import joblib
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

# Set the MLflow tracking server
mlflow.set_tracking_uri("http://mlflow:5000")  # Connect to MLflow container
mlflow.set_experiment("breast_cancer_experiment")

print("MLflow Tracking URI:", mlflow.get_tracking_uri())

# Load dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Standardize the data
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Function to perform hyperparameter search
def perform_search(model, param_grid, search_type='grid', n_iter=10):
    if search_type == 'grid':
        search = GridSearchCV(model, param_grid, cv=5, n_jobs=-1, verbose=1)
    else:
        search = RandomizedSearchCV(model, param_grid, n_iter=n_iter, cv=5, n_jobs=-1, verbose=1)
    
    search.fit(X_train, y_train)
    return search.best_estimator_, search.best_params_, search.best_score_

# Define models and hyperparameters
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

# Function to run ML experiments and log to MLflow
def run_experiment(model_name, model, param_grid, search_type='grid', use_random_search=False):
    with mlflow.start_run() as run:
        mlflow.log_param('model', model_name)
        mlflow.log_param('search_type', search_type)
        
        # Perform hyperparameter tuning
        search = 'random' if use_random_search else search_type
        best_model, best_params, best_score = perform_search(model, param_grid, search, n_iter=10)
        
        # Evaluate the model
        y_pred = best_model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        # Log parameters and metrics
        mlflow.log_params(best_params)
        mlflow.log_metric('accuracy', accuracy)
        
        # Log the model using mlflow.sklearn
        mlflow.sklearn.log_model(best_model, "model")
        
        print(f"✅ {model_name} trained - Best Params: {best_params}, Accuracy: {accuracy}")
        print(f"🏃 View run {run.info.run_id} at: {mlflow.get_tracking_uri()}/#/experiments/{run.info.experiment_id}/runs/{run.info.run_id}")
        print(f"🧪 View experiment at: {mlflow.get_tracking_uri()}/#/experiments/{run.info.experiment_id}")
        
        return best_model, best_params, accuracy

# Run the training process
for model_name, model in models.items():
    print(f"🚀 Running experiment with {model_name}...")
    run_experiment(model_name, model, param_grids[model_name], search_type='grid', use_random_search=False)

    print(f"🎯 Running experiment with {model_name} (Random Search)...")
    run_experiment(model_name, model, param_grids[model_name], search_type='random', use_random_search=True)
