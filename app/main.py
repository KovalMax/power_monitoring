from fastapi import FastAPI

from .controller import events

app = FastAPI()
app.include_router(events.router)
