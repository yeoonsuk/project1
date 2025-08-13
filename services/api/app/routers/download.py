from fastapi import APIRouter, UploadFilem, File
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/download/{task_id}")
async def download_image(task_id: str):
    
    #처리 완료된 이미지 파일을 클라이언트에 반환하는 역할.
    #실제론 S3에서 파일을 가져와서 스트리밍 응답해야 함.
    
    # TODO: S3에서 파일 읽어서 StreamingResponse로 반환
    
    # 임시 메시지 반환
    return {"task_id": task_id, "message": "download link placeholder"}