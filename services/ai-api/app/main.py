from fastapi import FastAPI
from app.routers import health, prompts

app = FastAPI(title="ai-api", version="0.1.0")

# mount routers
app.include_router(health.router, prefix="")
app.include_router(prompts.router, prefix="/prompts")