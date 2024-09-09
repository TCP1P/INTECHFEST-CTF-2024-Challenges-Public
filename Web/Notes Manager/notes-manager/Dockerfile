# Use an official Python runtime as the base image
FROM python:3.8.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the project dependencies
RUN pip install -r requirements.txt

# Copy the project files to the working directory
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Set the command to run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]