from pydantic import BaseModel

from diep_factory.types.boss import BossModel
from diep_factory.types.shape import ShapeModel
from diep_factory.types.tank import TankModel


class DiepPackModel(BaseModel):
  version: int
  """Format version of the diep pack"""
  name: str
  author: str
  tanks: list[TankModel] | None = None
  shapes: list[ShapeModel] | None = None
  bosses: list[BossModel] | None = None