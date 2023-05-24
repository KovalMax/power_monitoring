from os import environ

import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker

from app.model.event.power_state_update import PowerStateUpdateEvent

rabbitmq_broker = RabbitmqBroker(url=environ.get("BROKER_HOST"))
dramatiq.set_broker(rabbitmq_broker)


@dramatiq.actor
def power_state_update(update_event: dict[str, str | float]):
    e = PowerStateUpdateEvent(**update_event)
    print(e)



