#class harus punya nama
class Cat:
    # __init__ = constructor
    # fungsi pertama yng dipnggil
    # self = key khusus yng mengakseas internal class
    def __init__(self, color, height):
        # set attribute2 yng ada ke self
        self.color = color
        self.height = height

# buat objek (turunan dari class)
garfield = Cat("orange", 10)
persia= Cat("white", 7)

# cek objek dari kelas kucing
print("Obj garfield:", garfield.color, garfield.height)
print("Obj persia:", persia.color, persia.height)

# akses atribute dari objek
print(f"persia berwarna {persia.color}")
print(f"persia tinggi {persia.height} cm")
