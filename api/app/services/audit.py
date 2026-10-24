from typing import Any

from sqlmodel import Session

from app.models import RunEvent


def record_event(
    session: Session,
    *,
    intake_id: str,
    step: str,
    status: str,
    message: str,
    duration_ms: int | None = None,
    details: dict[str, Any] | None = None,
) -> RunEvent:
    event = RunEvent(
        intake_id=intake_id,
        step=step,
        status=status,
        message=message,
        duration_ms=duration_ms,
        details=details or {},
    )
    session.add(event)
    session.commit()
    session.refresh(event)
    return event
