from datetime import datetime
from os import environ
from typing import Annotated

from fastapi import APIRouter, Header, HTTPException
from starlette import status

from app.model.request.create_event_request import CreateStateEventRequest
from app.queue.worker import power_state_update

router = APIRouter(
    prefix="/api",
    tags=["events"],
    responses={404: {"description": "Not found"}, 201: {"description": "Created"}},
)


@router.post("/events", status_code=status.HTTP_201_CREATED)
async def create_state_event(req: CreateStateEventRequest, user_agent: Annotated[str | None, Header()] = None):
    if user_agent != environ.get("DEVICE_AGENT"):
        raise HTTPException(status_code=404, detail="Not found")

    if not req.fired_at:
        req.fired_at = datetime.utcnow().timestamp()

    power_state_update.send(req.dict())

    return {}
