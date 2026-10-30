from diep_factory import Barrel, DiepPack, Tank

LongGunTank = Tank().add_barrels(
  *reversed([Barrel(length=i*40, width_at_base=1, width_at_tip=(i*0.1)+1) for i in range(1,10)])
)

MyDiepPack = DiepPack(name="my diep pack", author="Generated with diep-factory")
MyDiepPack.add_tanks(LongGunTank)

print(MyDiepPack.build(indent=2))