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
  id: str | None = None
  """⚠ This ID gets transformed by diep to follow the format `custom_shape_{x}` in ascending index order."""
  
  name: str | None = None

  sides: Annotated[int | None, Field(gt=0)] = None

  size: Annotated[float | None, Field(gt=0,le=352)] = None
  """Max shape size is 5 squares in radius."""

  maxHealth: Annotated[float | None, Field(gt=0,le=1000000)] = None

  xpBounty: Annotated[float | None, Field(ge=0,le=10000000)] = None
  """The score given when this shape is killed."""

  damageOnTouch: Annotated[float | None, Field(ge=0,le=1000)] = None
  """The body damage of the shape."""

  knockbackOnTouch: Annotated[float | None, Field(ge=0,le=1000)] = None
  """How hard it shoves what it hits."""

  knockbackMultiplier: Annotated[float | None, Field(ge=0,le=3)] = None
  """How far a hit moves it."""

  color: str | None = None
  """A hex RGB code with the leading hashtag."""

  ai: ShapeAIModel | None = None
  """The movement of the shape."""

  spawn: ShapeSpawnModel | None = None
  """The spawning rules of the shape."""