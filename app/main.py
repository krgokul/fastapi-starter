import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotev import load_dotenv
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
async def health():
    return {"message": "Hello, World!"}


# Include Routes

# To run the application using Uvicorn programmatically
if __name__ == "__main__":
    HOST = os.getenv("API_HOST")
    PORT = int(os.getenv("API_PORT"))

    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
