"""Day 140: Custom Metaclasses and Registration."""

class PluginMeta(type):
    registry = {}

    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)
        if name != "BasePlugin":
            mcs.registry[name] = cls
        return cls

class BasePlugin(metaclass=PluginMeta):
    def run(self):
        raise NotImplementedError

class AudioPlugin(BasePlugin):
    def run(self):
        return "Audio"

class VideoPlugin(BasePlugin):
    def run(self):
        return "Video"

if __name__ == "__main__":
    assert "AudioPlugin" in PluginMeta.registry
    assert "VideoPlugin" in PluginMeta.registry
    print("Day 140 Metaclass tests passed!")
