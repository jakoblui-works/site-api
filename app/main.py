from fastapi import FastAPI

from app.core.sentry import init_sentry
from app.health.router import router as health_router

init_sentry()

app = FastAPI()

app.include_router(health_router)

