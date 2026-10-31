from typing import Self

from diep_factory.barrel import Barrel
from diep_factory.types.tank import TankModel


class Tank:
    def __init__(self, id: int | None = None, name: str = "Unnamed Tank"):
        self.id = id
        self.name = name
        self.barrels: list[Barrel] = []

    def build(self) -> TankModel:
        """Builds the tank and returns it as a Pydantic Model."""

        return TankModel(
            id = self.id,
            name = self.name,
            barrels = [barrel.build() for barrel in self.barrels]
        )

    def add_barrels(self, *barrels: Barrel) -> Self:
        self.barrels += barrels
        return self