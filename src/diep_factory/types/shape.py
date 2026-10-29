from typing import Annotated

from pydantic import BaseModel, Field


class ShapeAIModel(BaseModel):
  floatSpeed: Annotated[float | None, Field(ge=0,le=1000)] = None
  """
    The drift speed of the shape.
    If this shape is a crasher (hunts tanks), this field will be ignored.
  """

  aggressiveCrashRadius: Annotated[float | None, Field(gt=0,le=2000)] = None
  """
    The chase range of the crasher shape.
    If this field exists, the shape is automatically considered as a crasher (hunts tanks).
  """

  aggressiveCrashSpeed: Annotated[float | None, Field(ge=0,le=1000)] = None
  """
    The chase speed of the crasher shape.
    If this shape is not a crasher (hunts tanks), this field will be ignored.
  """

class ShapeSpawnModel(BaseModel):
  radiusMin: Annotated[float | None, Field(ge=0,le=1)] = None
  """Inner radius of the spawn zone."""

  radiusMax: Annotated[float | None, Field(ge=0,le=1)] = None
  """Outer radius of the spawn zone."""

  densityMultiplier: Annotated[float | None, Field(ge=0,le=1000)] = None
  """The spawn weight of the shape."""

class ShapeModel(BaseModel):
  id: str
  """⚠ This ID gets transformed by diep to follow the format `custom_shape_{x}` in ascending index order."""
  
  name: str

  sides: Annotated[int, Field(gt=0)]

  size: Annotated[float, Field(gt=0,le=352)]
  """Max shape size is 5 squares in radius."""

  maxHealth: Annotated[float, Field(gt=0,le=1000000)]

  xpBounty: Annotated[float, Field(ge=0,le=10000000)]
  """The score given when this shape is killed."""

  damageOnTouch: Annotated[float, Field(ge=0,le=1000)]
  """The body damage of the shape."""

  knockbackOnTouch: Annotated[float, Field(ge=0,le=1000)]
  """How hard it shoves what it hits."""

  knockbackMultiplier: Annotated[float, Field(ge=0,le=3)]
  """How far a hit moves it."""

  color: str
  """A hex RGB code with the leading hashtag."""

  ai: ShapeAIModel
  """The movement of the shape."""

  spawn: ShapeSpawnModel
  """The spawning rules of the shape."""