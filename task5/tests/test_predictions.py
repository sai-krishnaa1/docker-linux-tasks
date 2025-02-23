import requests
import logging

logging.basicConfig(level=logging.DEBUG)

# The base URL for the API
BASE_URL = "http://127.0.0.1:5000/predict"

def test_predict():
    # Sample input data (example Iris features)
    input_data = {
        "sepal length (cm)": 5.1,
        "sepal width (cm)": 3.5,
        "petal length (cm)": 1.4,
        "petal width (cm)": 0.2
    }
    
    # Send a POST request to the API
    response = requests.post(BASE_URL, json=input_data)
    logging.debug(f"Response status: {response.status_code}")
    logging.debug(f"Response content: {response.text}")
    
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Assert that the response contains a prediction
    response_data = response.json()
    assert 'prediction' in response_data

def test_predict_invalid():
    # Send a POST request with invalid data (no features)
    input_data = {}
    
    # Send request and log response
    response = requests.post(BASE_URL, json=input_data)
    logging.debug(f"Response status: {response.status_code}")
    logging.debug(f"Response content: {response.text}")
    
    # Assert that the response status code is 400 (Bad Request)
    assert response.status_code == 400