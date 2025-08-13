from fastapi import FastAPI
from .routers import upload, status, download

app = FastAPI()

app.include_router(upload.router)
app.include_router(status.router)
app.include_router(download.router)

@app.get("/")
def read_root():
    return {"message": "API 서버가 정상적으로 동작하고 있습니다."}

### dddd