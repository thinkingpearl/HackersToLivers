# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all backend files
COPY . .

# Expose the port your app runs on
EXPOSE 5000

# Command to run your app
CMD ["python", "appmain.py"]
