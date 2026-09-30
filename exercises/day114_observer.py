# Day 114: Observer Pattern (Pub/Sub)
from collections import defaultdict

class EventEmitter:
    def __init__(self):
        self._subscribers = defaultdict(list)

    def subscribe(self, event_type: str, callback):
        self._subscribers[event_type].append(callback)

    def emit(self, event_type: str, data):
        for callback in self._subscribers[event_type]:
            callback(data)

events = EventEmitter()
events.subscribe("user_signup", lambda user: print(f"Welcome email dispatched to {user}"))
events.subscribe("user_signup", lambda user: print(f"Metrics: incremented signups count for {user}"))

events.emit("user_signup", "Thanusha")
