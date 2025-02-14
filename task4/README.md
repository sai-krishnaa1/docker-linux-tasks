Here's the `README.md` file based on your request:

```markdown
# Titanic Airflow Preprocessing Project

This project demonstrates an Airflow-based pipeline for preprocessing the Titanic dataset. The pipeline consists of multiple tasks that include merging, cleaning, transforming, and splitting the dataset into train and test sets. The project uses Docker for containerization, with all dependencies specified in `requirements.txt`.

## Project Structure
task4/
├── dags/                        # Contains Airflow DAG files
│   ├── titanic_preprocessing.py  # The main Airflow DAG
├── data/                        # The data files
│   ├── cleaned.csv              # Cleaned data (after preprocessing)
│   ├── final_train.csv          # Final training dataset
│   ├── final_test.csv           # Final test dataset
│   ├── merged.csv               # Merged dataset
│   ├── test.csv                 # Test dataset (from Titanic dataset)
│   ├── train.csv                # Train dataset (from Titanic dataset)
│   ├── transformed_train.csv    # Transformed training data
│   ├── transformed_test.csv     # Transformed test data
├── docker-compose.yaml          # Docker Compose configuration
├── docker-compose.override.yml  # Docker Compose override (ignored by Git)
├── requirements.txt             # Python dependencies
├── scripts/                      # Preprocessing scripts
│   ├── clean_data.py            # Script for cleaning data
│   ├── merge_data.py            # Script for merging datasets
│   ├── split_data.py            # Script for splitting data
│   └── transform_data.py        # Script for transforming data
└── logs/                        # Airflow logs
```

## Steps to Reproduce the Project

### Prerequisites

Ensure the following are installed on your machine:
- **Docker**: Install Docker and Docker Compose. [Docker Installation Guide](https://docs.docker.com/get-docker/)
- **Git**: For version control and pushing the project to GitHub. [Git Installation Guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- **Python**: Required for dependencies listed in `requirements.txt`.

### Clone the Repository

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/titanic-airflow-preprocessing.git
   cd titanic-airflow-preprocessing
   ```

### Setup Docker Containers

2. **Run the Docker containers**:
   From the root of the project, run the following to start the Airflow containers using Docker Compose:
   ```bash
   docker-compose up --build
   ```
   This will:
   - Build the Docker images.
   - Start the containers for Airflow, PostgreSQL, and Redis.
   
   The Airflow UI will be accessible at `http://localhost:8080` (default username: `admin`, password: `admin`).

### Airflow DAG Execution

3. **Access Airflow UI**:
   Open your browser and go to `http://localhost:8080` to access the Airflow UI. Log in with the credentials (username: `admin`, password: `admin`).

4. **Trigger the DAG**:
   - In the Airflow UI, locate the `titanic_preprocessing` DAG.
   - Trigger the DAG manually by clicking on the play button.
   - Monitor the tasks as they execute. You can track the logs for each task.

### The Pipeline Tasks

The Airflow DAG `titanic_preprocessing.py` includes the following tasks:

1. **Merge Data**: Merges training and test datasets (train.csv, test.csv).
2. **Clean Data**: Performs data cleaning such as filtering and correcting data types.
3. **Split Data**: Splits the dataset into training and test sets, as well as cross-validation sets.
4. **Transform Data**: Applies any transformations such as feature engineering or one-hot encoding.

### Python Scripts

These preprocessing scripts are placed in the `scripts/` folder:

- **clean_data.py**: Handles the data cleaning process.
- **merge_data.py**: Merges the training and test data into a single dataset.
- **split_data.py**: Splits the dataset into training, validation, and testing sets.
- **transform_data.py**: Applies transformations like scaling, encoding, etc., to the dataset.

### Docker Configuration

- The project uses Docker to containerize the Airflow and PostgreSQL services.
- The `docker-compose.yaml` file sets up the services for Airflow, PostgreSQL, and Redis.

### Additional Setup

- **requirements.txt**: All necessary Python dependencies are listed here. After the containers are built, the required packages will be installed automatically.
- **Data**: The `train.csv` and `test.csv` are there  are inside the  `data/` folder.

## Cleanup

When done, you can stop the Docker containers with:
```bash
docker-compose down
```
This will stop and remove the containers, but the data and logs will persist.

## Contributing

Feel free to fork and contribute to this project. Ensure that any modifications follow the code style and best practices outlined in this repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

![Screenshot from 2025-02-14 20-04-21](https://github.com/user-attachments/assets/dc494815-b377-47c0-a3ab-564b47c4c182)
![Screenshot from 2025-02-14 20-04-44](https://github.com/user-attachments/assets/64258ca3-6798-4ec2-b738-47f27c3df5be)




This README file outlines the project structure, dependencies, and steps to reproduce and run the project. It provides a clear understanding of the Airflow DAG, Docker setup, and scripts involved.
