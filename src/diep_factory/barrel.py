import math
from typing import Self

from diep_factory.types.shared import BarrelModel

# TODO: add defaults

class Barrel:
  def __init__(
    self, 
    length: float | None = None,
    width_at_base: float | None = None,
    width_at_tip: float | None = None,
    angle: float | None = None,
    gap: float | None = None,
    offset: float | None = None
  ):
    self.set_length(length)
    self.set_width_at_base(width_at_base if width_at_base is not None else 1)
    self.set_width_at_tip(width_at_tip)
    self.set_angle(angle)
    self.set_gap(gap)
    self.set_offset(offset)


  def build(self) -> BarrelModel:
    """Builds the barrel and returns it as a Pydantic Model."""
    return BarrelModel(
      distance = self.length,
      heightMultiplier = self.width_at_base,
      muzzleScale = (
        (self.width_at_tip / self.width_at_base) 
        if self.width_at_tip is not None and self.width_at_base is not None 
        else None
      ),
      angle = self.angle,
      startDistance = self.gap,
      offset = self.offset
    )

  @staticmethod
  def from_model(barrel_model: BarrelModel) -> Barrel:
    return Barrel(
      length = barrel_model.distance,
      width_at_base = barrel_model.heightMultiplier,
      width_at_tip = (
        (barrel_model.muzzleScale * barrel_model.heightMultiplier)
        if barrel_model.muzzleScale is not None and barrel_model.heightMultiplier is not None
        else None
      ),
      angle = math.degrees(barrel_model.angle) if barrel_model.angle is not None else None,
      gap = barrel_model.startDistance,
      offset = barrel_model.offset
    )

  def set_length(self, length: float | None) -> Self:
    self.length = length
    return self

  def set_width_at_base(self, width_at_base: float | None) -> Self:
    self.width_at_base = width_at_base
    return self

  def set_width_at_tip(self, width_at_tip: float | None) -> Self:
    self.width_at_tip = width_at_tip
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
    self.gap = gap
    return self

  def set_offset(self, offset: float | None) -> Self:
    self.offset = offset
    return self