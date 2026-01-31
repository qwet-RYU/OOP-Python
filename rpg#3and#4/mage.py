from hero import Hero

# panggil parent class sebagai parameter
# child class = mewarisi semua atr dan method dari parent class
class Mage(Hero):
    # mendefinisikan job nya
    def __init__(self, name, hp, ):
        # super() = mengakses method dari parent class
        super().__init__(name, hp, job="Mage")

    # metgod baru khusus mage
    def cast_spell(self,):
        print(f"🔮{self.name} cast spell magic attack...")

    # timpa ultimate skill dari parent class
    def ultimate(self, enemy):
        dmg = 100
        print(f"💥{self.name} mengeluarkan ultimate skill: ATOMIC BOMB! | {dmg} DMG")
        # monster kena damage
        enemy.take_damage(dmg)