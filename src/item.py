from dataclasses import dataclass
from datetime import date

@dataclass
class Item:
    name: str
    price: float
    expire: date

    def description(self) -> str:
        return f'{self.name} {self.price}'