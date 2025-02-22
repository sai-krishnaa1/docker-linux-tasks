# Stage 1: Build the dependencies
FROM python:3.9-slim AS builder
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/

# Stage 2: Create the smaller final image
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /app/requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt && \
    mkdir -p /artifacts && \
    chmod 777 /artifacts && \
    mkdir -p /mlruns && \
    chmod 777 /mlruns

COPY --from=builder /app /app/
RUN rm -rf /root/.cache && \
    rm -rf /app/__pycache__

CMD ["python", "/app/train.py"]