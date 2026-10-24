from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session

from app.config import get_settings
from app.db import create_db_and_tables, engine
from app.services.seed import seed_demo_crm

settings = get_settings()


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    create_db_and_tables()
    with Session(engine) as session:
        seed_demo_crm(session)
    yield


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="Human-reviewed intake workflow using fictional demo data.",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.web_origin],
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT"],
    allow_headers=["Content-Type"],
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": settings.app_name}
