from collections.abc import Generator

from sqlmodel import Session, SQLModel, create_engine

from app.config import get_settings
from app import models as _models  # noqa: F401  # registers tables on SQLModel.metadata

settings = get_settings()
connect_args = (
    {"check_same_thread": False}
    if settings.database_url.startswith("sqlite")
    else {}
)

engine = create_engine(
    settings.database_url,
    connect_args=connect_args,
    echo=False,
)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
