import numpy as np


class Regurgitator:
    def __init__(self):
        self.initiated = True

    def hello(self, name: str) -> str:
        return f"Hello, {name}!"

    def goodbye(self, name: str) -> str:

        return f"Goodbye, {name} :("
