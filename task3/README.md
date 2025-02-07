Here’s the complete README file for the Task 3 project, following the project structure and the instructions you’ve provided:

---

# Task 3: Machine Learning Model Experimentation, Tracking, and Deployment

## Project Structure
```
docker-linux-tasks/      # Main project directory
│
├── task1/               # Task 1 directory (not part of Task 3)
├── task2/               # Task 2 directory (not part of Task 3)
└── task3/               # Task 3 directory (This README file)
    ├── artifacts/       # Directory containing model artifacts (trained models)
    │   ├── LogisticRegression_best_model.pkl
    │   ├── SVM_best_model.pkl
    │   └── RandomForest_best_model.pkl
    │
    ├── docker-compose.yml # Docker Compose file to run MLFlow server and model container
    ├── mlflow_runs/      # Directory containing MLFlow run results and experiment data
    ├── mlruns/           # Directory for storing MLFlow models and artifacts
    ├── src/              # Source code for the ML models and training process
    │   ├── Dockerfile    # Dockerfile for building the image to run the model
    │   ├── requirements.txt  # Python dependencies for the project
    │   └── train.py      # Python script to train, test, and log experiments with MLFlow
    └── README.md         # This file
```

## Overview

In Task 3, we focus on performing machine learning model experimentation, hyperparameter optimization, tracking the results using MLFlow, and creating a pseudo-release of the best model. This task involves creating multiple experiments with different features, models, and hyperparameters, followed by logging the results to MLFlow for comparison and analysis.

### Main Goals:
1. **Experimentation**: Run multiple experiments with different models, hyperparameters, and features.
2. **Hyperparameter Search**: Perform hyperparameter tuning using both grid search and random search.
3. **Model Tracking**: Log experiment results (accuracy, parameters, and model artifacts) to MLFlow for visualization and reproducibility.
4. **Pseudo-Release**: Clean and finalize the best model code and push it to a release branch/tag.
5. **Artifact Management**: Store the best model artifacts for future use.

### Task 3 File Details:

- **docker-compose.yml**: Defines two services – one for running the MLFlow server and the other for running the model container.
- **src/Dockerfile**: Defines how the model container image is built. It uses a two-stage build process to install dependencies and copy necessary files.
- **src/requirements.txt**: Lists the Python dependencies required for this task, including MLFlow and scikit-learn.
- **src/train.py**: The main script for training, testing, and logging machine learning models using MLFlow. It also handles the hyperparameter search and logging of the best models.
- **artifacts**: Contains the best-trained model files saved as `.pkl` files for Logistic Regression, SVM, and Random Forest.
- **mlflow_runs** and **mlruns**: Directories for storing MLFlow tracking data, experiments, and model artifacts.

## Steps to Run the Project

1. **Clone the Repository**:
   Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/docker-linux-tasks.git
   cd docker-linux-tasks
   ```

2. **Navigate to Task 3**:
   ```bash
   cd task3
   ```

3. **Navigate to the `src` Directory**:
   ```bash
   cd src
   ```

4. **Build the Docker Image**:
   Build the Docker image using the `Dockerfile`:
   ```bash
   docker build -t your-image-name .
   ```

5. **Run the Docker Containers**:
   First, make sure Docker Compose is set up and ready. Run the following command to start the MLFlow server and model container:
   ```bash
   docker-compose up --build
   ```

   This will start the MLFlow server on port 5000 and also run the model container which trains the models, performs hyperparameter search, and logs everything to MLFlow.

6. **Access MLFlow UI**:
   After the containers are up and running, you can view the experiment tracking and results at:
   ```
   http://localhost:5000
   ```

7. **Running Experiments**:
   The training script (`train.py`) will run experiments with multiple models, including:
   - **Logistic Regression**
   - **SVM (Support Vector Machine)**
   - **Random Forest**

   The script performs grid and random search hyperparameter tuning for each model, logs the results (accuracy, parameters, and artifacts) in MLFlow, and saves the best models as artifacts in the `artifacts` folder.

8. **Making a Pseudo-Release**:
   Once the best model is selected, make a clean release of the model code:
   ```bash
   git checkout -b release-v1.0
   git add .
   git commit -m "Finalized model code for release"
   git tag -a v1.0 -m "Release v1.0 - Best Model"
   git push origin release-v1.0
   ```

   This will tag the commit as version 1.0 and push the release branch to GitHub.

9. **Storing the Best Model Artifacts**:
   The best models are saved in the `artifacts/` directory as `.pkl` files. You can also track the model artifacts in the MLFlow server.

## Docker Setup and Services

- **MLFlow Server**: The `mlflow` service in `docker-compose.yml` starts an MLFlow server on port 5000, which you can access to visualize experiments and results.
- **Model Training**: The second service is used to run the model training and experiment tracking. It communicates with the MLFlow server to log experiments and models.

### Example Docker Compose Configuration

```yaml
version: '3.8'

services:
  mlflow:
    image: ghcr.io/mlflow/mlflow:v2.9.2
    container_name: mlflow_server
    ports:
      - "5000:5000"
    volumes:
      - ./mlflow_runs:/mlruns
    command: >
      mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root /mlruns --host 0.0.0.0 --port 5000
```

This configuration allows you to run the MLFlow server, where you can visualize the experiment tracking UI and manage the models.

## Requirements

To run this project, you need to have the following software installed:
- **Docker** and **Docker Compose**: For containerizing and running the MLFlow server and model training.
- **Python 3.9+**: For dependencies and model training.
- **MLFlow**, **scikit-learn**, **joblib**, **pandas**, **numpy**: These dependencies are specified in the `requirements.txt` file.

Install the Python dependencies by running:
```bash
pip install -r requirements.txt
```

## Conclusion

This project involves conducting machine learning experiments, logging results using MLFlow, and deploying the best model through Docker containers. By following the steps in the README, you will be able to track experiments, perform hyperparameter tuning, and make a clean release of the best model for further use.

---

This README provides a comprehensive overview of Task 3 and guides the user through the steps of running the experiment, tracking results, and managing the best model. Let me know if you need any modifications!
