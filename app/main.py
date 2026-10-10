from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Alfred Technologies"}

@app.get("/health")
def health():
    return {"status": "healthy"}