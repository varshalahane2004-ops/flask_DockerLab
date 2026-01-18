Flask Docker Lab

## Aim
To demonstrate Docker container, volume usage and data persistence with a simple Flask app.

## Description
- This project is a simple Flask app running inside a Docker container.
- Logs are stored in a Docker volume to persist data even if the container is deleted.
- Visiting the app URL generates timestamps in the log file.

## Files
- app.py : Flask application
- Dockerfile : Docker image instructions
- README.md : This file

## How to Run
1. Build Docker image:
2. create Docker volume
3. run container
4. open browser
5. http://localhost:5000
