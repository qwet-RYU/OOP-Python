class Hero:
    # pertama kali dipanggil / summon
    # self = diri sendiri / internal
    # \n untuk jarak
    def __init__(self, name, hp, job):
        self.name = name
        self.__hp = hp  # private attribute
        self.job = job
        # multi select ctrl+D
        print(f"Hero {self.name} telah disummon!")

    # getter ambil attr private
    # pola penulisan : get_namaAttr
    def get_hp(self):
        return self.__hp
    
    # setter ubah attr private
    #  pola penulisan : set_namaAttr
    def set_hp(self, addHp):
        self.__hp += addHp

    def take_damage(self, damage):
        # self.__hp = self.__hp - damage (aslinya)
        self.__hp -= damage
        print(f"{self.name} menerima {damage} damage!")
        print(f"❗Sisa HP : {self.__hp}")
        if self.__hp == 0:
            print(f"☠{self.name} telah gugur!")

    # fungsi heal
    def heal(self):
        print(f"✨{self.name} sedang recovery")
        heal_amount = 35
        self.__hp +=heal_amount
        print(f"✔HP {self.name} disembuhkan! +{heal_amount}")

    def attack(self, enemy):
        print(f"⚔{self.name} menyerang {enemy}!")

    #fungsi status
    def __str__(self):
        status = "❤  HIDUP"
        if self.__hp ==0:
            status =" ☠  MATI"

        return (f"[{self.job}] HP : {self.__hp} | {status}")
    
    # ultimate attack
    def ultimate(self, enemy):
        print(f"💥{self.name} bengong...")