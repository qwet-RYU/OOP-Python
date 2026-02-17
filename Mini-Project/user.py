
from encodings import undefined


class User:
    def __init__(self, nama, kamar, hari, tanggal, jam) -> None:
        self.nama = nama
        self.kamar = kamar
        self.hari = hari
        self.tanggal = tanggal
        self.jam = jam
        self.__status = 'menunggu konfirmasi'

    @property
    def status(self):
        return self.__status
    
    def diizinkan(self):
        self.__status = ' ✅ diizinkan'
        # hari minggu / ahad
        if self.hari == 'minggu' or self.hari == 'ahad':    
            return
    
    def tidak_diizinkan(self):
        self.__status = ' ❌ tidak diizinkan'
        # hari puasa
        if self.hari == 'senin' or self.hari == 'kamis':    
            return 
    
    def perizinan_bersyarat(self):
        self.__status = ' 🆗 perizinan bersyarat'
        # sore hari
        jam_jam = self.jam.split(':')[0].split('.')[0]  # '17.00' → '17'
        if int(jam_jam) >= 16 and int(jam_jam) < 17:
            return

    def tambah_izin(self):
        print(f"Mau Tambah Santri Lagi?.")
        jawaban = input("na-am/laa: ").strip().lower()  
        if jawaban in ['na-am', 'naam']:  
            return True
        return False 

    def komen_musyrif(self, komentar):
        print(f"Komentar Musyrif: {komentar}")
        return komentar
    
undefined