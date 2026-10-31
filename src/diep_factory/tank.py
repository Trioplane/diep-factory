from typing import Self

from diep_factory.barrel import Barrel
from diep_factory.types.tank import TankModel


class Tank:
  def __init__(
    self,
    id: int | None = None,
    name: str | None = "Unnamed Tank"
  ):
    self.set_id(id)
    self.set_name(name)
    self.barrels: list[Barrel] = []

  def build(self) -> TankModel:
    """Builds the tank and returns it as a Pydantic Model."""

    return TankModel(
      id = self.id,
      name = self.name,
      barrels = [barrel.build() for barrel in self.barrels]
    )

  @staticmethod
  def from_model(tank_model: TankModel) -> Tank:
    tank = Tank(
      name = tank_model.name
    )

    if tank_model.barrels is not None:
      tank.add_barrels(*[Barrel.from_model(barrel) for barrel in tank_model.barrels])

    return tank

  def set_name(self, name: str | None):
    self.name = name

  def set_id(self, id: int | None):
    self.id = id

  def add_barrels(self, *barrels: Barrel) -> Self:
    self.barrels += barrels
    return self