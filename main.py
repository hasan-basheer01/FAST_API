from fastapi import FastAPI

app = FastAPI()


# Root endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to my FastAPI application!"
    }


# Path parameter endpoint
@app.get("/greet/{name}")
def greet(name: str):
    return {
        "message": f"Hello, {name}!"
    }