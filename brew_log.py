# === Stage 1: Каркас модуля ===
# Project: BrewLog
from datetime import date
from dataclasses import dataclass, field
from typing import List


@dataclass
class Brew:
    name: str
    style: str
    volume: float
    date: date


def make_demo_brews() -> List[Brew]:
    return [
        Brew(name="Dunkelweizen", style="Weizen", volume=20.0, date=date(2025, 1, 11)),
        Brew(name="Amber Ale", style="Ale", volume=25.0, date=date(2025, 2, 3)),
        Brew(name="Porter", style="Stout", volume=19.0, date=date(2025, 3, 20)),
    ]


def print_brews(brews: List[Brew]) -> None:
    for brew in brews:
        print(f"{brew.date} | {brew.name} | {brew.style} | {brew.volume} л")


def main() -> None:
    brews = make_demo_brews()
    print("BrewLog — журнал домашней пивоварни")
    print(f"Создано рецептов: {len(brews)}")
    print_brews(brews)


if __name__ == "__main__":
    main()
