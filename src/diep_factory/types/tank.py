from typing import Annotated

from pydantic import BaseModel, Field

from diep_factory.types.shared import (
  BarrelModel,
  ProjectileModel,
  TankBodyModel,
  TankInvisibilityModel,
)


class TankModel(BaseModel):
  id: Annotated[int, Field(gt=100000)]
  """Custom tank IDs start at 100001, anything below is reserved for special use by the game."""

  name: str | None = None

  minLevel: int | None = None

  body: TankBodyModel | None = None

  projectiles: list[ProjectileModel] | None = None

  invisibility: TankInvisibilityModel | None = None

  statsMaxLevel: tuple[
    Annotated[int, Field(ge=0,le=12)],
    Annotated[int, Field(ge=0,le=12)],
    Annotated[int, Field(ge=0,le=12)],
    Annotated[int, Field(ge=0,le=12)],
    Annotated[int, Field(ge=0,le=12)],
    Annotated[int, Field(ge=0,le=12)],
    Annotated[int, Field(ge=0,le=12)],
    Annotated[int, Field(ge=0,le=12)],
  ] | None = None

  barrels: list[BarrelModel] | None = None