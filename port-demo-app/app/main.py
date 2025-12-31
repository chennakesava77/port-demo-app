from fastapi import FastAPI
import os

app = FastAPI()

APP_NAME = "Port Demo App"
PORT = os.getenv("PORT", "8000")

@app.get("/")
def root():
    return {
        "app_name": APP_NAME,
        "port": PORT
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
