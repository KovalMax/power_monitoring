from fastapi import APIRouter, Request, HTTPException, Body
from starlette import status

from app.dependencies.dependecies import get_notification_service

router = APIRouter(
    prefix="/api",
    tags=["telegram"],
    responses={403: {"description": "Forbidden"}, 201: {"description": "Created"}},
)

notification_service = get_notification_service()


@router.post("/telegram", status_code=status.HTTP_200_OK)
async def create_state_event(payload: dict = Body()):
    print(type(payload))
    print(payload)

    return {}

    user_id = json['text'].split(' ')[1]
    chat_id = json['chat']['id']

    print(user_id)
    print(chat_id)

    notification_service.save_chat_settings(user_id, chat_id)
    notification_service.send_telegram_message(chat_id, 'Сповіщення для телеграму налаштовано! U+2705')

    return {}
