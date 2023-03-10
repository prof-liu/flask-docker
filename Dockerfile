FROM python:3.9.6-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy requirements from local to docker image
COPY requirements.txt /app

# Install the dependencies in the docker image
RUN pip3 install -r requirements.txt --no-cache-dir

# Copy everything from the current dir to the image
COPY ./src .

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]