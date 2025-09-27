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

# Copy backend code
COPY backend/ /app

# Copy built frontend
COPY --from=frontend-builder /frontend/dist /app/static

# Copy environment variables
COPY .env /app/.env

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (optional but recommended)
EXPOSE 10000

# Start FastAPI
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=10000"]

