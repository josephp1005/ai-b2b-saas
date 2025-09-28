from fastapi import APIRouter
import logging

logger = logging.getLogger("ai-api")
logger.setLevel(logging.INFO)

router = APIRouter(tags=["health"])

@router.get("/health")
def health():
    logger.info("[ai-api] /health ping")
    return {"ok": True, "service": "ai-api"}
