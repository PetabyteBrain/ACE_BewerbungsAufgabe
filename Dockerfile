# Use an official lightweight Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements if you have one, otherwise install Flask directly
RUN pip install --no-cache-dir flask

# Copy your app code
COPY Api.py .

# Expose the internal port Flask runs on
EXPOSE 5000

# Run the app
CMD ["python", "Api.py"]

