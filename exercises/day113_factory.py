# Day 113: Factory Method Pattern
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> str:
        pass

class EmailNotifier(Notifier):
    def send(self, message: str) -> str:
        return f"[EMAIL] {message}"

class SMSNotifier(Notifier):
    def send(self, message: str) -> str:
        return f"[SMS] {message}"

class NotificationFactory:
    @staticmethod
    def get_notifier(channel: str) -> Notifier:
        if channel == "email":
            return EmailNotifier()
        elif channel == "sms":
            return SMSNotifier()
        raise ValueError(f"Unknown channel: {channel}")

notifier = NotificationFactory.get_notifier("email")
print(notifier.send("Deployment successful!"))
