# Hello World Python App


A simple Flask application that responds with a JSON greeting.

## Features

- Flask web server
- Health check endpoint
- JSON responses with timestamp and version info
- Dockerized for easy deployment
- Non-root user for security
- Gunicorn WSGI server for production

## Endpoints

- `GET /` - Returns hello world message with metadata
- `GET /health` - Health check endpoint

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

The app will be available at http://localhost:8080

## Docker

```bash
# Build the image
docker build -t hello-world-app .

# Run the container
docker run -p 8080:8080 hello-world-app
```

## Environment Variables

- `PORT` - Server port (default: 8080)
- `APP_VERSION` - Application version (default: 1.0.0)
# Updated Wed Jul  2 14:14:37 CEST 2025
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
