from hero import Hero

# panggil parent class sebagai parameter
# child class = mewarisi semua atr dan method dari parent class
# metgod baru khusus warrior
class Warrior(Hero):
    def __init__(self, name, hp, ):
        # super() = mengakses method dari parent class
        super().__init__(name, hp, job="Warrior")

    # timpa ultimate skill dari parent class
    def ultimate(self, enemy):
        dmg = 125
        print(f"💥{self.name} mengeluarkan ultimate skill: EXCALIBUR! | {dmg} DMG")
        # monster kena damage
        enemy.take_damage(dmg)