from fastapi import FastAPI

app = FastAPI()

@app.get("/b")
def hello():
    return {"hi"}