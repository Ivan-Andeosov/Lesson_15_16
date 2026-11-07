from fastapi import FastAPI
import random
import uvicorn

app = FastAPI()

@app.get("/")
def random_number():
    return {"number": random.randint(1, 100)}

