from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


class IntakeCreate(BaseModel):
    sample_id: str | None = None
    raw_text: str | None = Field(default=None, min_length=20, max_length=6_000)

    @model_validator(mode="after")
    def one_source(self) -> "IntakeCreate":
        supplied = [self.sample_id is not None, self.raw_text is not None]
        if sum(supplied) != 1:
            raise ValueError("Provide exactly one of sample_id or raw_text")
        return self


class RunEventRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    intake_id: str
    step: str
    status: str
    message: str
    duration_ms: int | None
    details: dict[str, Any]
    created_at: datetime


class IntakeListItem(BaseModel):
    id: str
    sample_id: str | None
    source_type: str
    status: str
    display_name: str
    matter_type: str
    warnings_count: int
    created_at: datetime


class IntakeDetail(BaseModel):
    id: str
    sample_id: str | None
    source_type: str
    raw_text: str
    status: str
    extraction: dict[str, Any] | None
    validation: dict[str, Any] | None
    final_record: dict[str, Any] | None
    reviewer_notes: str | None
    crm_contact_id: str | None
    created_at: datetime
    updated_at: datetime
    events: list[RunEventRead]


class DemoContactRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    display_name: str
    email: str | None
    phone: str | None
    matter_type: str | None
    opposing_parties: list[str]
    source_intake_id: str | None
    is_existing_client: bool
    created_at: datetime


class DemoSampleRead(BaseModel):
    id: str
    title: str
    description: str
    tags: list[Literal["complete", "missing", "conflict", "urgent", "adversarial"]]
