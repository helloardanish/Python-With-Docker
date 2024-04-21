# Use an official Python runtime as the base image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt


# Run main.py when the container launches
CMD ["python", "main.py"]


# Run Test.py when the container launches
CMD ["python", "Test.py"]
