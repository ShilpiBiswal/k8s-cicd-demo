# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expose app port
EXPOSE 5000

# Run app
CMD ["python", "app.py"]
