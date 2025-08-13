from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()

    ## TODO: services/s3_service.py의 함수를 호출하여 AWS S3에 파일 업로드

    return JSONResponse(content={"filename": file.filename, "size": len(contents)})
