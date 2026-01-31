
from mage import Mage
from warrior import Warrior
from monster import Monster

aldos = Warrior("Aldos", 100)
nana = Mage("Nana", 100)
dragon = Monster("Dragon King", 1000)

# updt attr hp
# ambil attr hp


print(aldos)
print(nana)
print(dragon)

nana.heal()
nana.cast_spell()
nana.ultimate(dragon)
aldos.ultimate(dragon)
# aldos.cast.spell()  # error, karena masih ngambil dari class Hero
print(dragon)