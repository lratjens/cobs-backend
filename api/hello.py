from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file in development
if os.getenv("VERCEL_ENV") != "production":
    load_dotenv()

app = FastAPI()

# Get the frontend URL from environment variable, fallback to a list of allowed origins
ALLOWED_ORIGINS = os.environ.get("ALLOWED_ORIGINS", "http://localhost:3000,https://cobs-frontend.vercel.app").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
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
