import os
import sys
from fastapi import FastAPI

# Read port from environment
PORT = os.getenv("APP_PORT")

if not PORT:
    print("ERROR: APP_PORT environment variable is not set", file=sys.stderr)
    sys.exit(1)

app = FastAPI()
PORT = int(PORT)

@app.get("/")
def root():
    return {
        "app": "port-demo-app",
        "port": PORT
    }

@app.get("/health")
def health():
    return {
        "status": "OK"
    }
