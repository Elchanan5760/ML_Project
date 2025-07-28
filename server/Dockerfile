# Use official Python image
FROM python:3.12-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# Expose the port where server will run
EXPOSE 8000

# Command to start training service
CMD ["uvicorn", "APIServer:app", "--host", "0.0.0.0", "--port", "8000"]




