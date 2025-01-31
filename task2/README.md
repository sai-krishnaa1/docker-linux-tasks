# Dockerized Diabetes Prediction Project

## Project Overview
This project demonstrates an end-to-end pipeline for predicting diabetes using Logistic Regression on the Pima Indians Diabetes dataset. The entire workflow is containerized using Docker, ensuring reproducibility and easy deployment.

---

## File Structure
```
/docker-linux-tasks/task2/
|-- Dockerfile            # Docker configuration to build the image
|-- requirements.txt      # Required Python packages for the project
|-- /shared               # Folder for shared files (e.g., dataset, predictions)
   |-- predictions.csv    # Predicted results output file
|-- diabetes.csv          # Pima Indians Diabetes dataset
|-- pima_model.pkl        # Trained Logistic Regression model
|-- inference.py          # Inference script to make predictions
|-- /app                  # Application files inside the Docker container
```

---

## Setup Instructions
Follow these steps to set up and run the project:

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/diabetes-prediction-docker.git
cd diabetes-prediction-docker
```

### 2. Build the Docker Image
```bash
docker build --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) -t myimage .
```

### 3. Verify the Image
```bash
docker images
```
Ensure `myimage` is listed in the available images.

---

## Running the Application

### 1. Start the Docker Container and Run the Inference Script
```bash
docker run -it --rm \
  --mount "type=bind,src=$(pwd)/shared,dst=/app/data" \
  myimage bash
```

### 2. Inside the Container, Run the Inference Script
```bash
python /app/inference.py
```

The script will generate a `predictions.csv` file inside the shared directory on the host machine.

### 3. View the Predictions on the Host Machine
```bash
cd shared
cat predictions.csv
```
Alternatively, you can open the `shared` directory in a file explorer to view the `predictions.csv` file.

---

## End-to-End Process

### 1. Data Collection and Preprocessing
**Dataset:** The Pima Indians Diabetes dataset contains medical information such as glucose level, BMI, age, and blood pressure for 768 patients. The target is whether or not a patient has diabetes.

**Preprocessing Steps:**
- Handled missing values (if any).
- Scaled features to ensure optimal model performance.

### 2. Model Development
- A Logistic Regression model was chosen for classification.
- `train.py` was created to:
  - Load the dataset.
  - Preprocess the data.
  - Train the Logistic Regression model.
  - Save the trained model as `pima_model.pkl`.

### 3. Inference Script
- `inference.py` was created to:
  - Load the saved model (`pima_model.pkl`).
  - Load new data for inference.
  - Generate predictions based on input data.
  - Save predictions to `predictions.csv` in the shared directory.

### 4. Containerization with Docker
- The project, including training and inference scripts, was containerized using Docker.
- `Dockerfile` was created to build the image, installing necessary dependencies and copying project files into the container.
- A multi-stage build was used to reduce the image size, and dependencies were installed in a separate layer to optimize caching.

### 5. Running the Application
- The `docker run` command starts the container and binds the shared directory on the host to the container’s data directory.
- This allows the script to save the `predictions.csv` file on the host machine.
- The `inference.py` script generates predictions for the dataset.

### 6. Output
- After running the inference script, predictions are saved as `predictions.csv` inside the shared folder.
- You can view the predictions using:
  ```bash
  cat shared/predictions.csv
  ```

---

## Model Performance
- **Model Used:** Logistic Regression
- **Accuracy:** 85% (or as per your final model training results)
- The model performs well as a baseline for diabetes prediction, providing a foundation for further improvements.

---

## Business Value
This model can be deployed in healthcare settings to predict diabetes in individuals, potentially leading to:

### 1. **Early Diagnosis**
- Helps healthcare professionals identify individuals at risk for diabetes early, allowing for timely intervention.

### 2. **Cost Reduction**
- Early prediction can reduce long-term treatment costs by preventing complications.

### 3. **Scalability**
- With Docker, this application can be easily deployed and scaled across different systems, providing flexibility and adaptability for healthcare providers.

---

## Conclusion
This project demonstrates an end-to-end workflow for diabetes prediction using Logistic Regression, Docker containerization, and a streamlined inference process. It provides a robust, reproducible, and scalable solution for healthcare analytics.

