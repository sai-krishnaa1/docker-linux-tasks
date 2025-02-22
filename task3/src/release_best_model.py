import mlflow
import os
from mlflow.tracking import MlflowClient

def release_best_model():
    # Connect to MLflow
    mlflow.set_tracking_uri("http://localhost:5000")
    client = MlflowClient()

    # Get all experiments
    experiment = client.get_experiment_by_name("breast_cancer_experiment")
    
    if experiment is None:
        raise Exception("No experiment found")

    # Get all runs for the experiment
    runs = client.search_runs(
        experiment_ids=[experiment.experiment_id],
        order_by=["metrics.accuracy DESC"]
    )

    if not runs:
        raise Exception("No runs found")

    # Get the best run
    best_run = runs[0]
    
    # Create release directory
    release_dir = "model_releases"
    os.makedirs(release_dir, exist_ok=True)

    # Since we're using local filesystem, construct the path using artifacts directory
    run_artifacts_dir = os.path.join('artifacts', '1', best_run.info.run_id, 'artifacts')
    
    if not os.path.exists(run_artifacts_dir):
        raise Exception(f"Artifacts directory not found at {run_artifacts_dir}")
    
    # Create model info file
    info_path = os.path.join(release_dir, "model_info.txt")
    with open(info_path, "w") as f:
        f.write(f"Best Model Information:\n")
        f.write(f"Run ID: {best_run.info.run_id}\n")
        f.write(f"Model Type: {best_run.data.params.get('model', 'Unknown')}\n")
        f.write(f"Accuracy: {best_run.data.metrics.get('accuracy', 0):.4f}\n")
        f.write(f"Parameters: {best_run.data.params}\n")

    print(f"Best model released to {release_dir}")
    print(f"Accuracy: {best_run.data.metrics.get('accuracy', 0):.4f}")
    print(f"Model Type: {best_run.data.params.get('model', 'Unknown')}")
    print(f"Artifacts location: {run_artifacts_dir}")
    print("\nNote: The model artifacts are available in the MLflow UI and in the artifacts directory.")

if __name__ == "__main__":
    release_best_model()