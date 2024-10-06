from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import os

app = FastAPI()

# Get the frontend URL from environment variable, fallback to localhost for local development
FRONTEND_URL = os.environ.get("FRONTEND_URL", "https://cobs-frontend.vercel.app")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "OK"}

@app.get("/api/hello")
async def hello():
    return {"message": f"Hello from the backend! Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"}
