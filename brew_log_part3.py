# === Stage 3: Хранилище в памяти ===
# Project: BrewLog
from dataclasses import dataclass, field
from datetime import date
from typing import List, Dict, Optional


@dataclass
class Brew:
    name: str
    style: str
    volume: float
    date: date
    id: Optional[str] = field(default=None, init=False)


class BrewStore:
    def __init__(self) -> None:
        self._items: Dict[str, Brew] = {}
        self._counter = 0

    def add(self, name: str, style: str, volume: float, date: date) -> Brew:
        self._counter += 1
        brew = Brew(name=name, style=style, volume=volume, date=date)
        brew.id = str(self._counter)
        self._items[brew.id] = brew
        return brew

    def get(self, brew_id: str) -> Optional[Brew]:
        return self._items.get(brew_id)

    def list_all(self) -> List[Brew]:
        return list(self._items.values())
