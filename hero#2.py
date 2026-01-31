class Hero:
    # pertama kali dipanggil / summon
    # self = diri sendiri / internal
    # \n untuk jarak
    def __init__(self, name, job, hp):
        self.name = name
        self.job = job
        self.hp = hp
        print(f"Hero {self.name} telah disummon!")

    def take_damage(self, damage):
        # self.hp = self.hp - damage (aslinya)
        self.hp -= damage
        print(f"{self.name} menerima {damage} damage!")
        print(f"❗Sisa HP : {self.hp}")
        if self.hp == 0:
            print(f"☠{self.name} telah gugur!")

    # fungsi heal
    def heal(self):
        print(f"✨{self.name} sedang recovery")
        heal_amount = 35
        self.hp +=heal_amount
        print(f"✔HP {self.name} disembuhkan! +{heal_amount}")

    def attack(self, enemy):
        print(f"⚔{self.name} menyerang {enemy}!")

    #fungsi status
    def __str__(self):
        status = "❤HIDUP"
        if self.hp ==0:
            status ="☠MATI"

        return (f"[{self.job}] HP : {self.hp} | {status}")

# buat objek / summon hero-hero ke lobby
zilong = Hero("Zilong", "Warrior", 100)
aurora = Hero("Aurora", "Mage", 100)
zilong.attack(aurora, 30)
print(aurora)
aurora.attack(zilong, 30)
print(zilong)
aurora.heal()