from discord import Webhook, RequestsWebhookAdapter
from config import AppConfig


class MotionDetectionNotifier:
    def __init__(self):
        self.webhook = Webhook.from_url(AppConfig.DISCORD_WEBHOOK_URL,
                                        adapter=RequestsWebhookAdapter())

    def send_message(self, message):
        self.webhook.send(content=message)
