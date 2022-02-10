# Nightmare
# by @yi64
#
# cheat sdk
import json

class Switch():
    def __init__(self, default=False) -> None:
        self.value = default
        self.cfg = None

    def switch(self):
        self.value != self.value

def read_config(key):
    config = json.load(open("config.json"))

    return config[key]

    
