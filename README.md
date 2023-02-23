# Flask-docker

## Installation & Usage

## Part 1

To use this project, start by cloning the repository:
```bash
git clone https://github.com/prof-liu/flask-docker.git
```

### Build the Docker image:
```bash
docker build -t exampleapp .
```
This will create a Docker image called exampleapp.

### Run the Docker container
```bash
docker run -p 5000:5000 exampleapp
```
This will start the container and map port 5000 on the host to port 5000 in the container.

Verify that the application is running properly by opening a web browser and navigating to http://localhost:5000. You should see a message that says "Hello, World!".

### Test the application (API)
There is one endpoint `/universities`, so let's test that out.
```
localhost:5000/universities?country=Germany
```

## Part 2

How to wrap your application into a new Docker image and push it to Docker Hub:

### Create a Docker Hub account 
Go to the Docker Hub website at https://hub.docker.com/ and click "Sign Up" to create an account.

### Log in to Docker Hub 
Using the docker login command in your terminal
Enter your Docker Hub credentials (username and password) when prompted.

```bash
docker login
```
### Tag the Docker image 
Tag the Docker image you just built with your Docker Hub username and the name of the new image you want to create. Replace your-dockerhub-username with your actual Docker Hub username, and exampleapp with the name of the new image you want to create.

```bash
docker tag exampleapp your-dockerhub-username/exampleapp
```

### Push the tagged Docker image to Docker Hub

```bash
docker push your-dockerhub-username/exampleapp
```
This will push the Docker image to Docker Hub, making it available for others to use.

### Verify on Docker Hub
Verify that the Docker image was pushed successfully by visiting the Docker Hub website and logging in to your account. You should see the exampleapp image listed in your repository.

Congratulations! You have now wrapped your application into a new Docker image and pushed it to Docker Hub. Others can now use your image by pulling it from Docker Hub using the docker pull command.
