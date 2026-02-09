from __future__ import annotations

class Hero:
    def __init__(self, name: str, role: str, hp: int, attack: int, heal: int, hero_type: str="hero"):
        self.name = name
        self.role = role
        self.max_hp = hp  
        self.hp = hp
        self.attack_power = attack
        self.heal_power = heal
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

    def heal(self):
        if not self.is_alive():
            print(f"❗ {self.name} sudah mati dan tidak bisa disembuhkan!")
            return
        heal_amount = self.heal_power
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

    def attack(self, name, enemy, damage=None):
        if damage is None:
            damage = self.attack_power
        print(f"⚔️  {self.name} menyerang {name} dengan ({damage} dmg!)")
        enemy.take_damage(damage)
        


    def rage_mode(self):
        if self.type == "boss" or self.type == "goblin" and self.hp <= self.max_hp / 2:
            self.attack_power *= 2
            print(f"👿 {self.name} Memasuki mode RAGE! Attack jadi {self.attack_power}!")

    def heal_friend(self, friend: Hero):
        if not self.is_alive():
            print(f"❗ {self.name} sudah mati dan tidak bisa menyembuhkan teman!")
            return
        heal_amount = self.heal_power
        friend.hp += heal_amount
        if friend.hp > friend.max_hp:
            friend.hp = friend.max_hp
        print(f"✨ {self.name} menyembuhkan {friend.name}. +{heal_amount} HP! Sisa: {friend.hp}")

    def __str__(self):
        status = "❤ HIDUP" if self.is_alive() else "☠ MATI"
        return f"[{self.role}] {self.name} | HP: {self.hp}/{self.max_hp} | {status}"

# Main program
heavy = Hero("Heavy", "Warrior", 160, 20, 25, "hero")
magister = Hero("Magister", "Mage", 110, 50, 0, "hero")
docter = Hero("Doctor", "Healer", 50, 10, 50, "hero")
goblin = Hero("Goblin", "Enemy", 120, 15, 0, "goblin")
boss = Hero("Raja Iblis", "Boss", 200, 50, 0, "boss")

print(f"dimensi lain telah terbuka... para Goblin menyerang! 🧛‍♂️")
print(f"Lindungi dunia ini dari mereka, Wahai {heavy}, {magister}, dan {docter}!🐱‍🏍")
print(f"Goblin memiliki status {goblin}")
goblin.attack(heavy.name, heavy, 30)
docter.heal_friend(heavy)
print(f"Status {heavy}")
print(f"Magister mengeluarkan mantra pemusnah dengan {magister.attack_power} damage!")
magister.attack(goblin.name, goblin)
print(f"Heavy mengeluarkan serangan Hammer Smash dengan {heavy.attack_power} damage!")
heavy.attack(goblin.name, goblin)
goblin.rage_mode()
print(f"Goblin menggunakan Fire Breath untuk Serangan Area dengan {goblin.attack_power} damage!")
goblin.attack(heavy.name, heavy)
goblin.attack(magister.name, magister)
goblin.attack(docter.name, docter)
print(f"Magister mengeluarkan Ultimate Destructo Ball dengan {magister.attack_power * 2} dmg!")
magister.attack(goblin.name, goblin, magister.attack_power * 2)
print(f"{boss} sudah muncul! 👹 saatnya tunjukkan kemampuanmu!")
print(f"Status {boss}")
print(f"Boss menggunakan Dark Slash dengan {boss.attack_power} damage!")
boss.attack(heavy.name, heavy)
docter.heal_friend(heavy)
docter.heal_friend(magister)
print(f"Heavy menggunakan Ultimate Ground Pound dengan {heavy.attack_power * 2} damage ke Boss!")
heavy.attack(boss.name, boss, heavy.attack_power * 2)
print(f"Magister mengeluarkan Ultimate Destructo Ball dengan {magister.attack_power * 2} dmg!")
magister.attack(boss.name, boss, magister.attack_power * 2)
boss.rage_mode()
print(f"Boss menggunakan Dark Storm dengan {boss.attack_power} damage ke semua hero!")
boss.attack(heavy.name, heavy)
boss.attack(magister.name, magister)
boss.attack(docter.name, docter)
print(f"Seluruh Manusia Percaya pada-Mu 🥺, Kalianlah Harapan Terakhir Dunia! 🌍")
print(f"Dengan Harapan Mereka 😼, Heavy dan Magister mengeluarkan Fusion Attack dengan {heavy.attack_power + magister.attack_power} damage!")
heavy.attack(boss.name, boss, heavy.attack_power + magister.attack_power)
print(f"Status {boss}")
print("🏆 Kalian Telah Berhasil Mengalahkan Goblin dan Raja Iblis! Akhirnya Dunia Terselamatkan! 🥳")
