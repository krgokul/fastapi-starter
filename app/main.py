import os
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.get("/api/health")
async def health():
    return {"message": "Hello, World!"}


# To run the application using Uvicorn programmatically
if __name__ == "__main__":
    HOST = os.getenv("HOST")
    PORT = int(os.getenv("PORT"))

    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
