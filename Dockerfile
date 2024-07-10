# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /chattypaws-backend

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Install PostgreSQL client
RUN apt-get update && apt-get install -y postgresql-client

# Copy the rest of the working directory contents into the container
COPY . .

# Install the image-processing-package
RUN pip3 install ./image-processing-package

# Make port 8001 available to the world outside this container
EXPOSE 8001

# Define environment variable
ENV DATABASE_URL=postgresql://${DATABASE_USERNAME}:${DATABASE_PASSWORD}@db/${DATABASE_NAME}

# Run create_tables.py to set up the database (optional, depending on your setup)
RUN python3 db/create_tables.py

# Run main.py when the container launches
CMD ["python3", "src/main.py"]
