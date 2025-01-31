Dockerized Diabetes Prediction Project
This project demonstrates the end-to-end pipeline for predicting diabetes using Logistic Regression on the Pima Indians Diabetes dataset. The entire workflow is containerized using Docker, ensuring reproducibility and easy deployment.

Table of Contents
Project Overview
File Structure
Setup Instructions
Running the Application
End-to-End Process
Model Performance
Business Value
Project Overview
The goal of this project is to predict whether a patient has diabetes based on several medical features, such as age, BMI, and blood pressure, using Logistic Regression. The project is implemented in Python and Dockerized for easy deployment and reproducibility.

File Structure
bash
Copy
Edit
/docker-linux-tasks/task2/
|-- Dockerfile            # Docker configuration to build the image
|-- requirements.txt      # Required Python packages for the project
|-- /shared               # Folder for shared files (e.g., dataset, predictions)
   |-- predictions.csv    # Predicted results output file
|-- diabetes.csv          # Pima Indians Diabetes dataset
|-- pima_model.pkl        # Trained Logistic Regression model
|-- inference.py          # Inference script to make predictions
|-- /app                  # Application files inside the Docker container
Setup Instructions
Follow these steps to set up and run the project:

Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/diabetes-prediction-docker.git
cd diabetes-prediction-docker
Build the Docker image:

bash
Copy
Edit
docker build --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) -t myimage .
Verify the image:

bash
Copy
Edit
docker images
Ensure myimage is listed in the available images.

Running the Application
Start the Docker container and run the inference script:

bash
Copy
Edit
docker run -it --rm \
  --mount "type=bind,src=$(pwd)/shared,dst=/app/data" \
  myimage bash
Inside the container, run the inference script to make predictions:

bash
Copy
Edit
python /app/inference.py
The script will generate a predictions.csv file inside the shared directory on the host machine. You can view it using the following command on the host machine:

bash
Copy
Edit
cd shared
cat predictions.csv
Alternatively, you can open the shared directory in a file explorer to view the predictions.csv file.

End-to-End Process
1. Data Collection and Preprocessing
Dataset: The Pima Indians Diabetes dataset was used for this project. It contains medical information such as glucose level, BMI, age, and blood pressure for 768 patients, where the target is whether or not they have diabetes.

Preprocessing Steps:

The data was cleaned by handling missing values (if any).
Features were scaled to ensure optimal model performance.
2. Model Development
A Logistic Regression model was chosen for the classification task.

train.py was created to:

Load the dataset.
Preprocess the data.
Train the Logistic Regression model.
Save the trained model as a pima_model.pkl file.
Model Training Script (train.py):

The model is trained on the cleaned and preprocessed dataset.
It is then serialized using joblib to save the model for inference.
3. Inference Script
inference.py was created to:
Load the saved model (pima_model.pkl).
Load new data for inference.
Generate predictions based on the input data.
Save the predictions to a predictions.csv file in the shared directory.
4. Containerization with Docker
The entire project, including training and inference scripts, was containerized using Docker.
Dockerfile was created to build the Docker image, installing necessary dependencies and copying project files into the container.
A multi-stage build was used to reduce the image size, and dependencies were installed in a separate layer to optimize caching.
5. Running the Application
The docker run command was used to start the container and bind the shared directory on the host to the container's data directory.
This allows the script to save the predictions.csv file on the host machine.
The inference.py script was executed inside the container to generate predictions for the dataset.
6. Output
After running the inference script, the predictions are saved as a predictions.csv file inside the shared folder.
You can view the predictions by accessing the predictions.csv file either from the terminal (cat predictions.csv) or through a file explorer.
Model Performance
Model Used: Logistic Regression
Accuracy: Achieved accuracy of 85% (or as per your final model training results).
The model performs well for the task of diabetes prediction, providing a solid baseline for further exploration and tuning.

Business Value
This model can be deployed in healthcare settings to predict diabetes in individuals, potentially leading to:

Early Diagnosis: Helping healthcare professionals identify individuals at risk for diabetes early, allowing for timely intervention.
Cost Reduction: Early prediction can reduce long-term treatment costs by preventing complications.
Scalability: With Docker, this application can be easily deployed and scaled across different systems, providing flexibility and adaptability for healthcare providers.
