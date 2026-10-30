import math
from typing import Self

from diep_factory.types.shared import BarrelModel


class Barrel:
  def __init__(
    self, 
    length: float,
    width_at_base: float,
    width_at_tip: float | None = None,
    angle: float | None = None,
    gap: float | None = None,
    offset: float | None = None
  ):
    self.set_length(length)
    self.set_width_at_base(width_at_base)
    self.set_width_at_tip(width_at_tip)
    self.set_angle(angle)
    self.set_gap(gap)
    self.set_offset(offset)


  def build(self) -> BarrelModel:
    """Builds the barrel and returns it as a Pydantic Model."""
    return BarrelModel(
      distance = self.distance,
      heightMultiplier = self.heightMultiplier,
      muzzleScale = self.muzzleScale,
      angle = self.angle,
      startDistance = self.startDistance,
      offset = self.offset
    )

  def set_length(self, length: float) -> Self:
    self.distance = length
    return self

  def set_width_at_base(self, width_at_base: float) -> Self:
    self.heightMultiplier = width_at_base
    return self

  def set_width_at_tip(self, width_at_tip: float | None) -> Self:
    self.muzzleScale = (width_at_tip / self.heightMultiplier) if width_at_tip is not None else None
    return self

  def set_angle(self, angle: float | None, radians: bool = False) -> Self:
    if angle is None:
      self.angle = None
      return self

    degrees = angle if not radians else math.degrees(angle)
    degrees = (degrees + 180) % 360 - 180

    self.angle = math.radians(degrees)
    return self

  def set_gap(self, gap: float | None) -> Self:
    self.startDistance = gap
    return self

  def set_offset(self, offset: float | None) -> Self:
    self.offset = offset
    return self

  