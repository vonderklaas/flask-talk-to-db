### Quick Start

Dockerfile 
```Dockerfile
# Pick Python version
FROM python:3.10-slim-buster

# Setup working directory
WORKDIR /flask-app

# Copy requirements.txt file into directory
COPY requirements.txt requirements.txt

# Install required dependencies
RUN pip install -r requirements.txt

# Copy the app to the container
COPY . .

# Init the database
RUN flask db init

# Generate migration scripts
RUN flask db migrate

# Apply the migrations to the database
RUN flask db upgrade

# Run the app
CMD ["python", "run.py"]
```

Build an image
```
docker build --tag <NAME> .
```

Run container from the image
```
docker run -d -p 5000:5000 <NAME>
```

Check if container is running
```
docker ps
```

Hit the app
```
GET http://localhost:5000/
```

When needed, stop the container
```
docker stop <CONTAINER>
```