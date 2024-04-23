from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "REST APP v1.0"}