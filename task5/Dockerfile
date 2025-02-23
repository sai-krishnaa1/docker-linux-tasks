# Use multi-stage build to reduce image size
FROM python:3.9-slim AS builder

# Set working directory
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project files needed for package installation
COPY requirements.txt .
COPY setup.py .
COPY src/ src/
COPY tests/ tests/

# Create virtual environment and install dependencies
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir pytest requests
RUN pip install --no-cache-dir -e .

# Final stage
FROM python:3.9-slim

# Install curl for healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy application files and tests
COPY src/ src/
COPY data/ data/
COPY tests/ tests/
COPY train_model.py .
COPY cron_batch.sh .

# Create non-root user for security
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app && \
    chmod +x cron_batch.sh

USER appuser

# Set environment variables
ENV PYTHONPATH=/app \
    FLASK_APP=src/api/app.py \
    FLASK_ENV=production

# Expose the API port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:5000/health || exit 1

# Command to run the Flask app
CMD ["python", "src/api/app.py"]