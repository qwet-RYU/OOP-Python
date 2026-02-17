from encodings import undefined
from user import User
from data import data_perizinan, simpan_data, load_data

class Musyrif(User):
    def __init__(self, nama_musyrif="Musyrif"):
        super().__init__("Musyrif", nama_musyrif, "", "", "")  # Dummy data
        self.nama_musyrif = nama_musyrif
        from data import data_perizinan 
        self.data = data_perizinan      



    def konfimasi_izin(self, user: User, keputusan: int) -> None:
        keputusan = int(keputusan)
        if user.status == 'menunggu konfirmasi' and user in data_perizinan:
            if keputusan == 1:
                user.diizinkan()
            elif keputusan == 2:
                user.tidak_diizinkan()
            elif keputusan == 3:
                user.perizinan_bersyarat()
            else:
                print("Keputusan tidak valid.")

    def komen_musyrif(self, komentar):
        print(f"Komentar Musyrif: {komentar}")
        return komentar
    
    def musyrif_pengizin(self, nama: str):   
        self.nama = nama
        return self.nama
    
    def verifikasi_izin(self, data_perizinan):
        if not data_perizinan:
            print("📭 Belum ada data perizinan untuk diverifikasi.")
            return
        
        for i, izin in enumerate(data_perizinan, 1):
            print(f"{i}. {izin.get('nama', 'N/A')} - {izin.get('status', 'pending')}")
        
        try:
            pilihan = int(input("Pilih nomor izin: ")) - 1
            if 0 <= pilihan < len(data_perizinan):
                izin_data = data_perizinan[pilihan]
                
                user = User(
                    izin_data['nama'],
                    izin_data['kamar'], 
                    izin_data.get('hari', ''),
                    izin_data['tanggal'], 
                    izin_data['jam']
                )
                
                print(f"\nReview {user.nama}: {user.status}")
                keputusan = input("Pilih Angka (1 ✅ Diizinkan, 2 ❌ Tidak Diizinkan, 3 🆗 Bersyarat): ")
                
                self.konfimasi_izin(user, keputusan)
            else:
                print("❌ Nomor izin tidak valid!")
        except ValueError:
            print("❌ Input harus berupa angka!")
        
        if keputusan == '1':
            user.diizinkan()
            print(f"✅ {user.nama} diizinkan")
        elif keputusan == '2':
            user.tidak_diizinkan()
            print(f"❌ {user.nama} tidak diizinkan")
        elif keputusan == '3':
            user.perizinan_bersyarat()
            print(f"🆗 {user.nama} bersyarat")
        else:
            print("❌ Keputusan tidak valid (1/2/3)!")

         
        komentar = input("Komentar musyrif: ")
        self.komen_musyrif(komentar)
            
            
        data_perizinan[pilihan]['status'] = user.status
        data_perizinan[pilihan]['musyrif_Pengizin'] = self.nama_musyrif
        data_perizinan[pilihan]['komentar_musyrif'] = komentar 
            
        print(f"✅ {user.status}")
        print(f"   Musyrif: {self.nama_musyrif}")
        print(f"   Komen: {komentar}")
        
simpan_data()
undefined