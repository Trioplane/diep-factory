import time
from typing import Self

import rich
from rich.progress import Progress, track

from diep_factory.barrel import Barrel
from diep_factory.tank import Tank
from diep_factory.types.base import DiepPackModel
from diep_factory.types.boss import BossModel
from diep_factory.types.shape import ShapeModel

DIEP_PACK_FORMAT_VERSION = 2

__all__ = [
    "Barrel",
    "DiepPack",
    "Tank"
]

class DiepPack:
    def __init__(self, name: str = "Unnamed Pack", author: str = "Unknown Author"):
        self.name = name
        self.author = author
        self.tanks: list[Tank] = []
        self.shapes: list[ShapeModel] = []
        self.bosses: list[BossModel] = []

    def build(self, indent: int | None = None) -> str:
        """Builds the pack and returns it as a JSON string."""

        rich.print(f"\n[cyan]Building [bright_cyan]'{self.name}' [cyan]by [bright_cyan]'{self.author}'\n")

        with Progress() as tank_progress:
            tanks = []
            tank_count = len(self.tanks)
            
            current_tank = tank_progress.add_task("[cyan]Building...", total=tank_count)

            for (index, tank) in enumerate(self.tanks):
                has_id = f" (ID {tank.id})" if tank.id else ""
                tank_progress.update(current_tank, description=f"[cyan]Building tank: [bright_cyan]{tank.name}[dim]{has_id} ({index+1}/{tank_count})")
                tanks.append(tank.build())
                tank_progress.update(current_tank, advance=1)

        diep_pack = DiepPackModel(
            version = DIEP_PACK_FORMAT_VERSION,
            name = self.name,
            author = self.author,
            tanks = tanks,
            shapes = self.shapes,
            bosses = self.bosses
        )

        rich.print(f"\n[green]Successfully built [bright_green]'{self.name}' [green]by [bright_green]'{self.author}'\n")

        return diep_pack.model_dump_json(indent=indent, exclude_none=True)

    def add_tanks(self, *tanks: Tank) -> Self:
        self.tanks += tanks
        return self