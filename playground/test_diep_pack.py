import random
import math

from diep_factory import Barrel, DiepPack, Tank

barrel_count = 26
TestingTank = Tank(name="Testing Tank").add_barrels(*[
  Barrel(
    length = random.uniform(10, 80),
    width_at_base = random.uniform(0.1, 1),
    width_at_tip = random.uniform(0.1, 1),
    gap = random.uniform(0, 100),
    offset = random.uniform(0, 200),
    angle = random.uniform(-180, 180)
  ) for i in range(barrel_count)
])

MyDiepPack = DiepPack(name="my diep pack", author="Generated with diep-factory")
MyDiepPack.add_tanks(TestingTank)

print(MyDiepPack.build())