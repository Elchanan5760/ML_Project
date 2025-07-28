FROM python:3.10-slim


# Set the working directory in the container
WORKDIR /app

COPY ../requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Copy the application code into the container



CMD ["uvicorn", ":app", "--host", "localhost", "--port", "8000"]




