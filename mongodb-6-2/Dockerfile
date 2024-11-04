# Base image with Python
FROM python:3.11.0

# Set working directory
WORKDIR /app

# Copy application code to container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
