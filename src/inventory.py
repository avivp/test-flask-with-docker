from dataclasses import dataclass
from item import Item
from datetime import date
from typing import Optional


class Inventory:

    def __init__(self):
        self.items = dict()
        self.items[1] = Item("item1", 2, date(2022, 12, 12))
        self.items[2] = Item("item2", 5, date(2022, 12, 12))

    def get(self, item_id: int) -> Optional[Item]:
        if item_id in self.items:
            return self.items[item_id]
        return None
