from pathlib import Path

from diep_factory import Barrel, DiepPack, Tank

MyDiepPack = DiepPack(name="my diep pack", author="Generated with diep-factory")

tank_count = 26
MyDiepPack.add_tanks(*[
  Tank(name=f"Tank {i}")
    .add_barrels(
      *[
        Barrel(length=80,angle=(360/tank_count)*j)
        for j in range(i)
      ]
    )
  for i in range(tank_count)
])

output_path = Path(__file__).resolve().parent / "output.diep-pack"

output_path.touch()
output_path.write_text(MyDiepPack.build(indent=2), encoding='utf8')

input_path = Path(__file__).resolve().parent / "input.diep-pack"
TestDiepPack = DiepPack.from_json(input_path.read_text())

for tank in TestDiepPack.tanks:
  for barrel in tank.barrels:
    barrel.set_length(
      (barrel.length if barrel.length is not None else 0) + 100
    )

print(TestDiepPack.build())