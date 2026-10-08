"""Day 156: Event Bus Pattern."""
from collections import defaultdict

class EventBus:
    def __init__(self):
        self._subscribers = defaultdict(list)

    def subscribe(self, event_type, handler):
        self._subscribers[event_type].append(handler)

    def publish(self, event_type, payload):
        for handler in self._subscribers[event_type]:
            handler(payload)

if __name__ == "__main__":
    bus = EventBus()
    received = []
    bus.subscribe("order_created", lambda data: received.append(data["id"]))
    bus.publish("order_created", {"id": 101})
    assert received == [101]
    print("Day 156 Event Bus tests passed!")
