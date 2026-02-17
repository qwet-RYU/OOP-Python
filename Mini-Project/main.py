from musyrif import Musyrif
from santri import Santri
from user import User
from data import data_santri, data_perizinan, simpan_data, load_data
from tabulate import tabulate

def display_data(data_perizinan):
    if not data_perizinan:
        print("📭 Belum ada data")
        return
    
    table = []
    for izin in data_perizinan:
        table.append([
            izin.get('no_izin', 'N/A'),
            izin.get('nama', 'N/A'),
            izin.get('kamar', 'N/A'),
            izin.get('hari', 'N/A'),
            izin.get('tanggal', 'N/A'),
            izin.get('jam', 'N/A'),
            izin.get('status', 'N/A'),
            izin.get('musyrif_Pengizin', ''),
            izin.get('komentar_musyrif', '')
        ])
    
    headers = ["No", "Nama", "Kamar", "Hari", "Tanggal", "Jam", "Status", "Musyrif", "Komentar"]
    print(tabulate(table, headers=headers, tablefmt="grid"))


def main():
    load_data()  # AUTO LOAD JSON/TXT
    
    while True:
        print("\n=== SISTEM PERIZINAN KELUAR PONDOK ===")
        print("1. Login Santri (Ajukan Izin)")
        print("2. Login Musyrif (Verifikasi Izin)")
        print("3. Lihat Semua Izin") 
        print("4. Keluar")
        
        aksi = 0
        while True:
            try:
                aksi = int(input("Pilih Aksi-Mu (1-4): "))
                if 1 <= aksi <= 4:
                    break
                print("❌ Pilih 1-4 SAJA!")
            except ValueError:
                print("❌ ANGKA 1-4 SAJA!")
        
        if aksi == 1:
            while True:  
                print("\n👨‍🎓 MODE SANTRI")
                nama = input("Nama Santri: ")
                kamar = input("Kamar Santri: ")
                hari = input("Hari Izin: ")
                tanggal = input("Tanggal Izin: ")
                jam = input("Jam Izin: ")
                
                santri = Santri(nama, kamar, hari, tanggal, jam)
                izin, tambah_lagi = santri.minta_izin(nama, kamar, hari, tanggal, jam)
        
                
                data_perizinan.append({
                    "no_izin": len(data_perizinan) + 1,  
                    "nama": nama,
                    "kamar": kamar,
                    "hari": hari,  
                    "tanggal": tanggal,
                    "jam": jam,
                    "status": izin.status,
                    "musyrif_Pengizin": ""
                })

                simpan_data()
                print("✅ Izin diajukan & tersimpan!")
        
                if not tambah_lagi:  
                    break

            
        elif aksi == 2:
            print("\n👨‍🏫 MODE MUSYRIF")
            nama_musyrif = input("Nama Musyrif (Enter=Ustadz Admin): ").strip() or "Ustadz Admin"
            musyrif = Musyrif(nama_musyrif)  
            musyrif.verifikasi_izin(data_perizinan)  
            simpan_data()
            
        elif aksi == 3:
            print("\n📋 SEMUA DATA IZIN")
            display_data(data_perizinan)  
            input("\n[Enter]...")
            
        elif aksi == 4:
            simpan_data()  # FINAL SAVE
            print("👋 Terima kasih! Data tersimpan permanen.")
            break
        
        input("\n[Enter] menu utama...")

if __name__ == "__main__":
    main()
