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
    - Calculated as `0.04 / time_to_vanish`.
  """

  lossOnHit: Annotated[float, Field(ge=0,le=1)]
  """
    How much to subtract from the invisibility percentage per hit.

    Equivalent to the 'Hits to reveal' setting in the editor.
    - Calculated as `min(1, 0.3 / (hits - 1))`. 
    - If `hits` is above 50, the value is treated as `never` or `0` meaning it will never lose invisibility per hit.
  """


class BarrelModel(BaseModel):
  distance: Annotated[float | None, Field(ge=5,le=500)] = None
  """Length of the barrel."""

  heightMultiplier: Annotated[float | None, Field(ge=0.1,le=2.5)] = None
  """
    Width of the gun.

    Equivalent to the 'Width at base' setting in the editor.
  """

  muzzleScale: Annotated[float | None, Field(ge=0.1,le=2.5)] = None
  """
    Width of the muzzle.

    Equivalent to the 'Width at tip' setting in the editor.
    - Calculated as `tip / base`.
  """

  bulletType: Literal[ProjectileType, "none"] | None = None
  
  projectile: Annotated[int | None, Field(ge=0)] = None