from typing import Annotated

from fastapi import APIRouter, Header, Request
from starlette import status

router = APIRouter(
    prefix="/api",
    tags=["telegram"],
    responses={403: {"description": "Forbidden"}, 201: {"description": "Created"}},
)


@router.post("/telegram", status_code=status.HTTP_201_CREATED)
async def create_state_event(request: Request, user_agent: Annotated[str | None, Header()] = None):
    print(request.body())
    print(user_agent)

    return {}
