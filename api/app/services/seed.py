from sqlmodel import Session, select

from app.models import DemoContact


# Data only. New DemoContact rows are built on insert so a test database
# and the app database never share the same Python object.
EXISTING_CLIENTS = [
    {
        "display_name": "Northstar Logistics LLC",
        "email": "operations@northstar.example",
        "matter_type": "business",
    },
    {
        "display_name": "Evelyn Brooks",
        "email": "evelyn.brooks@example.com",
        "matter_type": "estate",
    },
    {
        "display_name": "Apex Property Group",
        "email": "legal@apexproperty.example",
        "matter_type": "real_estate",
    },
]


def seed_demo_crm(session: Session) -> None:
    existing = session.exec(
        select(DemoContact).where(DemoContact.is_existing_client == True)  # noqa: E712
    ).first()
    if existing:
        return

    for client in EXISTING_CLIENTS:
        session.add(DemoContact(**client, is_existing_client=True))
    session.commit()
