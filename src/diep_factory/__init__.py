import rich
from pydantic import ValidationError
from typing import Self

from diep_factory.types.base import DiepPackModel
from diep_factory.types.boss import BossModel
from diep_factory.types.shape import ShapeModel
from diep_factory.types.shared import BarrelModel
from diep_factory.types.tank import TankModel

DIEP_PACK_FORMAT_VERSION = 2

class DiepPack:
    def __init__(self, name: str = "Unnamed Pack", author: str = "Unknown Author"):
        self.name = name
        self.author = author
        self.tanks: list[Tank] = []
        self.shapes: list[ShapeModel] = []
        self.bosses: list[BossModel] = []

        self.id_counter = {
            "tank": 0,
            "shapes": 0,
            "bosses": 0,
        }

    def build(self, indent: int | None = None) -> str:
        """Builds the pack and returns it as a JSON string."""
        diep_pack = DiepPackModel(
            version = DIEP_PACK_FORMAT_VERSION,
            name = self.name,
            author = self.author,
            tanks = [tank.build() for tank in self.tanks],
            shapes = self.shapes,
            bosses = self.bosses
        )

        return diep_pack.model_dump_json(indent=indent, exclude_none=True)

    def add_tanks(self, *tanks: Tank) -> Self:
        self.tanks += tanks
        return self

class Tank:
    def __init__(self, id: int | None = None, name: str = "Unnamed Tank"):
        self.id = id
        self.name = name
        self.barrels: list[Barrel] = []

    def build(self) -> TankModel:
        """Builds the tank and returns it as a Pydantic Model."""

        barrels: list[BarrelModel] = []
        for (index, barrel) in enumerate(self.barrels):
            try:
                barrels.append(barrel.build())
            except ValidationError as err:
                has_id = f" (ID: {self.id})" if self.id is not None else ""
                rich.print(f"\n[red]Error whilst building tank [cyan]'{self.name}'{has_id} [red]on [cyan]barrel {index}:\n")
                raise SystemExit(err)

        return TankModel(
            id = self.id,
            name = self.name,
            barrels = barrels
        )

    def add_barrels(self, *barrels: Barrel) -> Self:
        self.barrels += barrels
        return self

class Barrel:
    def __init__(
        self, 
        length: float,
        width_at_base: float,
        width_at_tip: float | None = None
    ):
        self.length = length
        self.width_at_base = width_at_base
        self.width_at_tip = width_at_tip if width_at_tip is not None else width_at_base

    def build(self) -> BarrelModel:
        """Builds the barrel and returns it as a Pydantic Model."""
        return BarrelModel(
            distance = self.length,
            heightMultiplier = self.width_at_base,
            muzzleScale = self.width_at_tip / self.width_at_base
        )