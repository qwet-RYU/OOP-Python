class Hero:
    def __init__(self, name, role, hp, attack, heal, hero_type="hero"):
        self.name = name
        self.role = role
        self.max_hp = hp  
        self.hp = hp
        self.attack = attack
        self.heal = heal
        self.type = hero_type
        print(f"✨ {self.name} ENTER LOBBY!")

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        print(f"💥 {self.name} menerima {damage} damage!")
        print(f"❗ Sisa HP: {self.hp}")
        if self.hp <= 0:
            self.hp = 0  # Clamp ke 0
            print(f"☠ {self.name} telah gugur!")

    def heal(self, ):
        if not self.is_alive():
            print(f"❗ {self.name} sudah mati dan tidak bisa disembuhkan!")
            return
        heal_amount = self.heal
        self.hp += heal_amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"✨ {self.name} sedang recovery. +{heal_amount} HP! Sisa: {self.hp}")
        if self.role == "Warrior":
            extra = 10
            self.hp += extra
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            print(f"✔ Warrior bonus: +{extra} HP! Total sisa: {self.hp}")

    def attack(self, enemy, boss):
        damage = self.attack
        print(f"⚔️ {self.name} menyerang {enemy.name, boss.name}!")
        enemy.take_damage(damage)


    def rage_mode(self):
        if self.type == "boss" and self.hp <= self.max_hp / 2:
            self.attack *= 2
            print(f"👿 {self.name} Memasuki mode RAGE! Attack jadi {self.attack}!")

    def __str__(self):
        status = "❤ HIDUP" if self.is_alive() else "☠ MATI"
        return f"[{self.role}] {self.name} | HP: {self.hp}/{self.max_hp} | {status}"

# Main program
heavy = Hero("Heavy", "Warrior", 150, 35, 25, "hero")
magister = Hero("Magister", "Mage", 100, 50, 0, "hero")
docter = Hero("Doctor", "Healer", 80, 20, 25, "hero")
goblin = Hero("Goblin", "Enemy", 120, 15, 0, "goblin")
boss = Hero("Raja Iblis", "Boss", 200, 50, 0, "boss")

print(f"dimensi lain telah terbuka... para Goblin menyerang! 🧛‍♂️")
print(f"Lindungi dunia ini dari mereka, Wahai {heavy}, {magister}, dan {docter}!🐱‍🏍")
print(f"Goblin memiliki status {goblin}")
docter.heal(heavy)
goblin.attack(heavy, 40)
print(f"Status {heavy}")
print(f"{boss} sudah muncul! 👹 saatnya tunjukkan kemampuanmu!")



