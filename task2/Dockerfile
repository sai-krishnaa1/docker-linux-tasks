# Stage 1: Build stage
FROM python:3.9-slim AS build

# Set working directory
WORKDIR /app

# Install required dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libatlas-base-dev \
&& rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt and install dependencies
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt --target /app/packages

# Stage 2: Final stage (for inference)
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Ensure the /app/data directory exists
RUN mkdir -p /app/data

# Copy installed Python dependencies from build stage
COPY --from=build /app/packages /app/packages
ENV PYTHONPATH=/app/packages

# Copy the model, dataset, and inference script
COPY diabetes.csv /app/
COPY pima_model.pkl /app/
COPY inference.py /app/

# Add a non-root user with the same UID/GID as the host system
ARG USER_ID
ARG GROUP_ID
RUN addgroup --gid $GROUP_ID user && \
    adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user

USER user

# Ensure the user has access to /app/data directory after container starts
CMD ["sh", "-c", "chown -R user:user /app/data && python /app/inference.py"]
