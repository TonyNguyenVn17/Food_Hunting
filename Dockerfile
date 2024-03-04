# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set working directory to /app
WORKDIR /app
ADD . /app

# Install packages 
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python3", "bot.py"]