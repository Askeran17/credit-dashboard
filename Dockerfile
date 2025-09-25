# step 1: build frontend
FROM node:20.19.0 AS frontend-builder

WORKDIR /frontend
COPY frontend/ /frontend
RUN npm install && npm run build

# step 2: backend
FROM python:3.10

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libssl-dev \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the backend code into the container
COPY backend/ /app

# Copy the built frontend
COPY --from=frontend-builder /frontend/dist /app/static

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start FastAPI with Uvicorn
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=10000"]
