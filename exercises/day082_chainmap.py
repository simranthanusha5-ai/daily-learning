# Day 82: ChainMap and Advanced Collections
from collections import ChainMap

defaults = {"theme": "light", "user": "guest", "debug": False}
user_prefs = {"theme": "dark"}
cli_args = {"debug": True}

# Scoped priority lookup: CLI > User > Defaults
config = ChainMap(cli_args, user_prefs, defaults)
print("Effective theme:", config["theme"])
print("Effective debug:", config["debug"])
print("Effective user:", config["user"])
