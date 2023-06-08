from typing import Annotated

from fastapi import APIRouter, Header
from starlette import status

router = APIRouter(
    prefix="/api",
    tags=["telegram"],
    responses={403: {"description": "Forbidden"}, 201: {"description": "Created"}},
)


@router.post("/telegram", status_code=status.HTTP_201_CREATED)
async def create_state_event(req, user_agent: Annotated[str | None, Header()] = None):
    print(req)
    print(user_agent)

    return {}
