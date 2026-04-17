from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return JSONResponse(content={"message": "API is running"}, status_code=200)

@app.get("/health")
def health():
    return JSONResponse(content={"message": "healthy"}, status_code=200)

@app.get("/me")
def me():
    return JSONResponse(content={
        "name": "IFIOK EMMANUEL",
        "email": "ifiokbassey.e@gmail.com",
        "github": "https://github.com/Wyze-digit"
    }, status_code=200)
