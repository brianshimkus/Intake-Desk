from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from sqlalchemy import Column, JSON, Text
from sqlmodel import Field, SQLModel


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def new_id() -> str:
    return str(uuid4())


class Intake(SQLModel, table=True):
    id: str = Field(default_factory=new_id, primary_key=True)
    sample_id: str | None = Field(default=None, index=True)
    source_type: str = Field(default="sample", index=True)
    raw_text: str = Field(sa_column=Column(Text, nullable=False))
    status: str = Field(default="received", index=True)

    extraction: dict[str, Any] | None = Field(
        default=None,
        sa_column=Column(JSON, nullable=True),
    )
    validation: dict[str, Any] | None = Field(
        default=None,
        sa_column=Column(JSON, nullable=True),
    )
    final_record: dict[str, Any] | None = Field(
        default=None,
        sa_column=Column(JSON, nullable=True),
    )
    reviewer_notes: str | None = Field(default=None, sa_column=Column(Text))
    crm_contact_id: str | None = Field(default=None, index=True)

    created_at: datetime = Field(default_factory=utc_now, index=True)
    updated_at: datetime = Field(default_factory=utc_now)


class RunEvent(SQLModel, table=True):
    id: str = Field(default_factory=new_id, primary_key=True)
    intake_id: str = Field(foreign_key="intake.id", index=True)
    step: str = Field(index=True)
    status: str = Field(index=True)
    message: str
    duration_ms: int | None = None
    details: dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSON, nullable=False),
    )
    created_at: datetime = Field(default_factory=utc_now, index=True)


class DemoContact(SQLModel, table=True):
    id: str = Field(default_factory=new_id, primary_key=True)
    display_name: str = Field(index=True)
    email: str | None = Field(default=None, index=True)
    phone: str | None = None
    matter_type: str | None = Field(default=None, index=True)
    opposing_parties: list[str] = Field(
        default_factory=list,
        sa_column=Column(JSON, nullable=False),
    )
    source_intake_id: str | None = Field(default=None, index=True)
    is_existing_client: bool = Field(default=False, index=True)
    created_at: datetime = Field(default_factory=utc_now)
