# use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the backend code into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start FastAPI with Uvicorn
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=10000"]
