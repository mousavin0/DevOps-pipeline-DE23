
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose the application port
EXPOSE 5000

# Define environment variable for Flask
ENV FLASK_APP=app.py


  
# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]
