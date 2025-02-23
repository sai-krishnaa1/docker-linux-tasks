# Model Deployment Project

This project demonstrates model deployment in two modes: online (REST API) and batch processing (scheduled pipeline). It uses Flask for the REST API and cron for batch scheduling.

## Project Structure
```
task5/
│── .dockerignore
│── tasky5 (venv)
│── cron_batch.sh
│── Dockerfile
│── README.md
│── requirements.txt
│── setup.py
│── train_model.py
│
│── data/
│   ├── input/
│   │   ├── batch_data.csv
│   │   ├── training_data.csv
│
│── src/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── app.py
│   ├── batch/
│   │   ├── __init__.py
│   │   ├── pipeline.py
│   ├── model/
│   │   ├── __init__.py
│   │   ├── model_loader.py
│   │   ├── artifacts/
│   │   │   ├── model.joblib
│
│── tests/
    ├── __init__.py
    ├── test_predictions.py
    ├── test_batch_pipeline.py
```

## Prerequisites
- Docker installed on your system
- Python 3.9+ (for local development)
- Git (for version control)

## Setup and Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd task5
```

2. Build the Docker image:
```bash
docker build -t model-deployment .
```

3. Run the container:
```bash
docker run -d -p 5000:5000 --name model-app model-deployment
```

## Verification Steps

### 1. Check Container Status
```bash
docker ps
```
Ensure the container is running and health check is passing.

### 2. Test REST API
Test the prediction endpoint:
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"sepal length (cm)": 5.1, "sepal width (cm)": 3.5, "petal length (cm)": 1.4, "petal width (cm)": 0.2}'
```

Expected response:
```json
{"prediction": 0}
```

### 3. Test Batch Processing
Access the container and run the batch script:
```bash
docker exec -it model-app bash
./cron_batch.sh
```

Verify batch predictions:
```bash
ls -l data/output/batch_predictions.csv
```

### 4. Run Tests
Execute the test suite:
```bash
docker exec -it model-app bash -c "python -m pytest tests/ -v"
```

### 5. Performance Verification
Check API response time:
```bash
time curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"sepal length (cm)": 5.1, "sepal width (cm)": 3.5, "petal length (cm)": 1.4, "petal width (cm)": 0.2}'
```
Response time should be << 1 second.

## Component Details

### Online Prediction (REST API)
- Endpoint: `http://localhost:5000/predict`
- Method: POST
- Input: JSON with four features
- Output: JSON with prediction

### Batch Processing
- Script: `cron_batch.sh`
- Input: `data/input/batch_data.csv`
- Output: `data/output/batch_predictions.csv`

### Model Information
- Type: Scikit-learn classifier
- Input features: 4 (sepal length, sepal width, petal length, petal width)
- Output: Class prediction (0, 1, or 2)

## Troubleshooting

1. If container fails to start:
```bash
docker logs model-app
```

2. If tests fail:
```bash
docker exec -it model-app bash
python -m pytest tests/ -v -s
```

3. If batch processing fails:
- Check if input data exists: `ls -l data/input/batch_data.csv`
- Verify model file: `ls -l src/model/artifacts/model.joblib`
- Check permissions: `ls -l cron_batch.sh`

## Clean Up
```bash
docker stop model-app
docker rm model-app
```

## Development

For local development:
1. Create virtual environment:
```bash
python -m venv tasky5
source tasky5/bin/activate  # Linux/Mac
# or
.\tasky5\Scripts\activate  # Windows
```

2. Install dependencies:
```bash
pip install -e .
pip install -r requirements.txt
```

3. Run tests locally:
```bash
python -m pytest tests/ -v
```

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request