from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "YouTube Agent API is running"}