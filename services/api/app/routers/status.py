from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/status/{task_id}")
async def get_status(task_id: str):
    
    # URL 경로의 task_id를 문자열 변수로 받음.
    # 실제 서비스에서는 DB에서 해당 작업의 처리 상태를 조회해서 반환.
    
    # TODO: DB에서 상태 조회 후 리턴
    
    # 임시로 'processing' 상태 반환
    return {"task_id": task_id, "status": "processing"}