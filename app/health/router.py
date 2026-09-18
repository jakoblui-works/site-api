from fastapi import APIRouter

from app.core.schemas import StatusResponse

router = APIRouter()

@router.get("/health", response_model=StatusResponse)
async def health_check():
    return {"status": "ok"}
