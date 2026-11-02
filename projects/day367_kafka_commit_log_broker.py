"""Day 367: Kafka-Style Commit Log."""

class Partition:
    def __init__(self):
        self.records = []

    def append(self, msg):
        offset = len(self.records)
        self.records.append(msg)
        return offset

    def fetch(self, offset, max_records=10):
        return self.records[offset:offset + max_records]

class MiniKafkaBroker:
    def __init__(self):
        self.topics = {}
        self.consumer_offsets = {} # (group, topic, part) -> offset

    def produce(self, topic, part_id, msg):
        self.topics.setdefault(topic, {}).setdefault(part_id, Partition())
        return self.topics[topic][part_id].append(msg)

    def consume(self, group, topic, part_id, max_records=5):
        key = (group, topic, part_id)
        current_offset = self.consumer_offsets.get(key, 0)
        part = self.topics.get(topic, {}).get(part_id, Partition())
        batch = part.fetch(current_offset, max_records)
        self.consumer_offsets[key] = current_offset + len(batch)
        return batch

if __name__ == "__main__":
    broker = MiniKafkaBroker()
    broker.produce("orders", 0, "order_1")
    broker.produce("orders", 0, "order_2")
    msgs = broker.consume("workers", "orders", 0)
    assert msgs == ["order_1", "order_2"]
    print("Day 367 Kafka Broker tests passed!")
