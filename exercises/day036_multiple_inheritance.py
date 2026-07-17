# Day 36: Multiple Inheritance and MRO

class JSONSerializable:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class Loggable:
    def log(self):
        print(f"[LOG] {self.__class__.__name__}: {self.__dict__}")

class ConfigRecord(JSONSerializable, Loggable):
    def __init__(self, env: str, debug: bool):
        self.env = env
        self.debug = debug

cfg = ConfigRecord("production", False)
cfg.log()
print("JSON representation:", cfg.to_json())
print("MRO:", [cls.__name__ for cls in ConfigRecord.__mro__])
