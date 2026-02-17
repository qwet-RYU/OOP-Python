from user import User

class Santri(User):

    def minta_izin(self, nama, kamar, hari, tanggal, jam) :
        izin = User(nama, kamar, hari, tanggal, jam)
        print(f" Status Izin: {izin.status}")  
        tambah_santri = self.tambah_izin()
        return izin, tambah_santri
