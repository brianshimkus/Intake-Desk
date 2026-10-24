from sqlmodel import Session, SQLModel, create_engine, select
from sqlmodel.pool import StaticPool

from app.models import DemoContact
from app.services.seed import seed_demo_crm


def test_seed_is_idempotent() -> None:
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        seed_demo_crm(session)
        seed_demo_crm(session)
        contacts = session.exec(select(DemoContact)).all()

    assert len(contacts) == 3
    assert all(contact.is_existing_client for contact in contacts)
