#!/bin/bash

# Get the directory of the current script
PROJECT_DIR="$(dirname "$(realpath "$0")")"

# Run the batch prediction Python script using an absolute path
python "$PROJECT_DIR/src/batch/pipeline.py"
