from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return("Hello From Plexios Casino API")