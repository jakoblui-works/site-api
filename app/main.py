from fastapi import FastAPI
from app.health.router import router as health_router
from app.core.sentry import init_sentry
from app.core.config import settings

init_sentry()

app = FastAPI()

app.include_router(health_router)

