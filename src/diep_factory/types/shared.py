from typing import Annotated, Literal

from pydantic import BaseModel, Field


class TankBodyModel(BaseModel):
  sides: Annotated[int, Field(ge=0,le=18)]

type ProjectileType = Literal["bullet", "drone", "trap"]

class ProjectileModel(BaseModel):
  name: str = "Unnamed Projectile"
  base: ProjectileType
  sides: Annotated[int, Field(ge=-1,le=18)] = -1

  # WIP

class TankInvisibilityModel(BaseModel):
  enabled: bool | None = None

  gain: Annotated[float, Field(ge=0.04 / 60, le=0.04 / 1)]
  """
    How much to add to the invisibility percentage per tick.

    Equivalent to the 'Time to vanish' setting in the editor. 
    - Calculated as `0.04 / x` where `x` is the time to vanish. 
  """

  lossOnHit: Annotated[float, Field(ge=0,le=1)]
  """
    How much to subtract from the invisibility percentage per hit.

    Equivalent to the 'Hits to reveal' setting in the editor.
    - Calculated as `min(1, 0.3 / (x - 1))` where `x` is the amount of hits. 
    - If `x` is above 50, the value is treated as `never` or `0` meaning it will never lose invisibility per hit.
  """

class BarrelModel(BaseModel):
  ...