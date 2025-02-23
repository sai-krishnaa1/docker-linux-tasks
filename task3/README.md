# Breast Cancer Classification with MLflow

## Project Overview
This project implements a machine learning pipeline for breast cancer classification using multiple models and hyperparameter optimization. The implementation uses MLflow for experiment tracking and Docker for containerization, ensuring reproducibility and easy deployment.

## Features
- Multiple model implementations (RandomForest, SVM, LogisticRegression)
- Automated hyperparameter optimization using Grid Search and Random Search
- Experiment tracking with MLflow
- Containerized environment using Docker
- Automated model selection and release process
- Comprehensive model performance tracking and visualization

## Project Structure
```
src/
├── train.py                # Main training script
├── release_best_model.py   # Script for releasing best model
├── requirements.txt        # Python dependencies
├── Dockerfile             # Container definition
└── docker-compose.yml     # Container orchestration
```

## Prerequisites
- Docker and Docker Compose
- Python 3.9 or higher (for local development)
- Git

## Installation & Setup

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Navigate to the source directory:
```bash
cd src
```

3. Create necessary directories:
```bash
mkdir -p artifacts mlruns
chmod 777 artifacts mlruns
```

## Running the Project

1. Start the MLflow server and training process:
```bash
docker-compose up --build
```

2. Access the MLflow UI:
- Open your web browser
- Navigate to http://localhost:5000
- View experiments, metrics, and artifacts

3. Release the best model:
```bash
python release_best_model.py
```

## Model Training Details

### Models Implemented
1. Random Forest Classifier
   - Grid Search and Random Search optimization
   - Parameters optimized: n_estimators, max_depth, min_samples_split, min_samples_leaf

2. Support Vector Machine (SVM)
   - Grid Search and Random Search optimization
   - Parameters optimized: C, kernel

3. Logistic Regression
   - Grid Search and Random Search optimization
   - Parameters optimized: C, solver

### Hyperparameter Optimization
- Grid Search: Exhaustive search over specified parameter values
- Random Search: Randomized search over parameter distributions

## Experiment Tracking

All experiments are tracked using MLflow, including:
- Model parameters
- Training metrics (accuracy)
- Model artifacts
- Best performing model selection

## Results

The project automatically tracks and compares the performance of different models. The best performing model is automatically selected based on accuracy metrics and can be accessed through the release script.

Best performing model metrics:
- Model: Logistic Regression
- Accuracy: 0.9912
- Parameters: {'C': 0.1, 'solver': 'liblinear'}

