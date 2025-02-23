---

# **Breast Cancer Classification with MLflow**

## **Project Overview**
This project implements a **machine learning pipeline for breast cancer classification** using multiple models and hyperparameter optimization. It leverages **MLflow** for experiment tracking and **Docker** for containerization, ensuring **reproducibility** and **easy deployment**.

---

## **Key Features**
✅ Multiple model implementations: **RandomForest, SVM, Logistic Regression**  
✅ Automated **hyperparameter optimization** (Grid Search & Random Search)  
✅ **Experiment tracking** with MLflow (metrics, parameters, artifacts)  
✅ **Containerized environment** using Docker for consistency  
✅ Automated **best model selection and release process**  
✅ **Performance visualization** and model comparison  

---

## **Project Structure**
```
src/
├── train.py                # Main training script (runs multiple experiments)
├── release_best_model.py   # Script to release the best model (saves artifacts)
├── requirements.txt        # Python dependencies
├── Dockerfile              # Defines containerized environment
└── docker-compose.yml      # Manages multi-container setup (MLflow & model server)
```

---

## **Prerequisites**
Before running the project, ensure you have the following installed:

- **Docker & Docker Compose** (for containerization)
- **Python 3.9+** (for local development, optional)
- **Git** (for version control)

---

## **Installation & Setup**
1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd <repository-name>
   ```
2. Navigate to the source directory:
   ```bash
   cd src
   ```
3. Create necessary directories for storing artifacts:
   ```bash
   mkdir -p artifacts mlruns
   chmod 777 artifacts mlruns  # Ensure write permissions
   ```

---

## **Running the Project**
### **1️⃣ Start the MLflow Server and Model Training**
Run the following command to build and start the containers:
```bash
docker-compose up --build
```
This will:
- Start an **MLflow tracking server**
- Train multiple models using **RandomForest, SVM, and Logistic Regression**
- Perform **hyperparameter tuning** (Grid Search & Random Search)
- Log **metrics, parameters, and artifacts** to MLflow

### **2️⃣ Access the MLflow UI**
- Open your browser and go to:
  ```
  http://localhost:5000
  ```
- View **experiments, metrics, and model artifacts**.

### **3️⃣ Release the Best Model**
After training, select the best-performing model and store it:
```bash
python release_best_model.py
```
This script:
- Selects the **best model based on accuracy**
- Saves its **artifacts (model weights, parameters, environment)**
- Prepares the model for deployment

---

## **Model Training Details**
### **Models Implemented**
1. **Random Forest Classifier**
   - Optimization: **Grid Search & Random Search**
   - Tuned Parameters: `n_estimators`, `max_depth`, `min_samples_split`, `min_samples_leaf`
  
2. **Support Vector Machine (SVM)**
   - Optimization: **Grid Search & Random Search**
   - Tuned Parameters: `C`, `kernel`
  
3. **Logistic Regression**
   - Optimization: **Grid Search & Random Search**
   - Tuned Parameters: `C`, `solver`

---

## **Hyperparameter Optimization**
| Method       | Description |
|-------------|------------|
| **Grid Search**  | Exhaustively searches over a predefined set of hyperparameters. |
| **Random Search** | Randomly samples hyperparameters from a distribution to find an optimal configuration. |

---

## **Experiment Tracking with MLflow**
Each experiment is automatically logged in **MLflow**, including:
- **Model parameters**
- **Training metrics** (e.g., accuracy)
- **Model artifacts** (saved models, configs, etc.)
- **Best-performing model selection**

---

## **Results & Best Model Selection**
The project tracks and compares different models. The **best model** is automatically selected based on accuracy.

| **Best Model** | **Accuracy** | **Optimized Parameters** |
|---------------|-------------|--------------------------|
| Logistic Regression | **0.9912** | `C=0.1, solver=liblinear` |

The selected model is stored in `artifacts/best_model/`.

---

## **Reproducibility & Deployment**
✅ **Reproducible Experiments**:  
All training runs and configurations are logged in MLflow, ensuring experiments can be re-run with the same parameters.

✅ **Two Running Containers**:
- **MLflow Server** (tracks experiments)
- **Model Pipeline** (runs training & releases best model)

✅ **Visualizations & Reports**:
- **MLflow UI** for comparing models

---

## **Task Requirements & Implementation**
| **Task** | **Implementation** |
|----------|--------------------|
| **1. Multiple Experiments** | Ran different models, hyperparameter tuning, and feature variations. |
| **2. MLflow Tracking** | Logged all metrics, parameters, and artifacts in MLflow. |
| **3. Best Model Release** | Created a script (`release_best_model.py`) to store the best model. |
| **4. Artifacts Storage** | Best model artifacts are saved for deployment. |

---
