from fastapi import FastAPI

from .controller import events, telegram

app = FastAPI()
app.include_router(events.router)
app.include_router(telegram.router)
