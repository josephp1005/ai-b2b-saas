from fastapi import APIRouter
from pydantic import BaseModel
import logging

logger = logging.getLogger("ai-api")
logger.setLevel(logging.INFO)

router = APIRouter(prefix="", tags=["prompts"])

class PromptIn(BaseModel):
    text: str
    user_id: str | None = None

@router.post("/prepare")
def prepare(p: PromptIn):
    logger.info("[ai-api] /prompts/prepare body=%s", p.model_dump())
    return {"prepared": True, "tokens_estimate": 42, "echo": p.model_dump()}

@router.post("/score")
def score(p: PromptIn):
    logger.info("[ai-api] /prompts/score body=%s", p.model_dump())
    return {"score": 0.5, "echo": p.model_dump()}