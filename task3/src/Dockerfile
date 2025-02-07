# Stage 1: Build the dependencies
FROM python:3.9-slim AS builder

# Set working directory
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt /app/

# Install dependencies without cache to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code to the working directory
COPY . /app/

# Stage 2: Create the smaller final image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt from builder
COPY --from=builder /app/requirements.txt /app/

# Install dependencies in the final stage
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the necessary files from the builder stage
COPY --from=builder /app /app/

# Clean up unnecessary files to keep the image lean
RUN rm -rf /root/.cache && \
    rm -rf /app/__pycache__

# Set the command to run the training script
CMD ["python", "/app/train.py"]
