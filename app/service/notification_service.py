import os

import requests

from app.firebase.firebase_client import FireBaseClient
from app.model.domain.models import EventModel, DeviceModel
from app.model.enum.power_state import PowerStateEnum
from app.redis.redis_client import RedisClient


class NotificationService:
    POWER_STATE_CACHE_PREFIX = 'events:state'
    SETTINGS_COLLECTION = 'UserSettings'
    BOT_TOKEN = os.environ.get('TG_BOT_TOKEN')
    TELEGRAM_API = 'https://api.telegram.org'
    SEND_MESSAGE = 'sendMessage'

    def __init__(self, redis_client: RedisClient, firebase_client: FireBaseClient):
        self.redis_client = redis_client
        self.firebase_client = firebase_client

    def send_notification(self, model: EventModel, device: DeviceModel):
        state_key = self.__get_key(model.device_id)
        state_entry = self.redis_client.get(state_key)
        if state_entry is None:
            self.redis_client.set(state_key, model.power_state.value)
            return

        if int(state_entry) != model.power_state.value:
            self.redis_client.set(state_key, model.power_state.value)
            settings = self.firebase_client.client\
                .collection(self.SETTINGS_COLLECTION)\
                .document(device.user_id).get().to_dict()

            if not settings['useTelegram']:
                return

            if model.power_state is PowerStateEnum.POWER_ON:
                self.send_telegram_message(
                    settings['chatId'], f'Зміна стана світла! {device.name}({device.location}) - Cвітло зʼявилось')
            else:
                self.send_telegram_message(
                    settings['chatId'], f'Зміна стана світла! {device.name}({device.location}) - Cвітло пропало')

    def save_chat_settings(self, user_id: str, chat_id: str):
        snapshot = self.firebase_client.client.collection(self.SETTINGS_COLLECTION).document(user_id)
        snapshot.update({'chatId': chat_id})

    def send_telegram_message(self, chat_id: str, message: str):
        url = f'{self.TELEGRAM_API}/bot{self.BOT_TOKEN}/{self.SEND_MESSAGE}'
        requests.get(url, params={'chat_id': chat_id, 'text': message})

    def __get_key(self, key_value: str) -> str:
        return f'{self.POWER_STATE_CACHE_PREFIX}:{key_value}'
