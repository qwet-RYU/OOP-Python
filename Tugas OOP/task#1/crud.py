from tabulate import tabulate
from data import data_list

def tambah_data():
    """Tambah data animasi baru"""
    id_baru = len(data_list) + 1
    nama_animasi = input("Masukkan nama animasi: ")
    nama_mc = input("Masukkan nama MC: ")
    
    data_baru = {
        "id": id_baru,
        "animasi": nama_animasi,
        "MC": nama_mc
    }
    data_list.append(data_baru)  # ← TAMBah ke list
    print(f"✅ Data {nama_animasi} berhasil ditambahkan!")

def hapus_data():
    """Hapus data berdasarkan ID"""
    tampilkan_data()
    try:
        id_hapus = int(input("Masukkan ID yang ingin dihapus: "))
        for i, animasi in enumerate(data_list):
            if animasi["id"] == id_hapus:
                data_list.pop(i)  # ← HAPUS dari list
                print(f"✅ Data ID {id_hapus} berhasil dihapus!")
                return
        print("❌ ID gak bener!")
    except ValueError:
        print("❌ ID harus angka!")

def ubah_data():
    """Ubah data berdasarkan ID"""
    tampilkan_data()
    try:
        id_ubah = int(input("Masukkan ID yang ingin diubah: "))
        for animasi in data_list:
            if animasi["id"] == id_ubah:
                print(f"Data lama: {animasi['animasi']} - {animasi['MC']}")
                animasi["animasi"] = input("Nama animasi baru: ") or animasi["animasi"]
                animasi["MC"] = input("MC baru: ") or animasi["MC"]
                print("✅ Data berhasil diubah!")
                return
        print("❌ ID tidak ditemukan!")
    except ValueError:
        print("❌ ID harus angka!")


def tampilkan_data():
    """Tampilkan semua data dengan tabulate - SUPER RAPI!"""
    if not data_list:
        print("❌ Data kosong!")
        return
    
    # list tabulate
    table_data = []
    for animasi in data_list:
        table_data.append([
            animasi["id"],
            animasi["animasi"],
            animasi["MC"]
        ])
    
    # Tampilkan dengan tabulate
    print("\n📺 DAFTAR ANIMASI")
    print(tabulate(
        table_data, 
        headers=["ID", "Animasi", "MC"], 
        tablefmt="grid"  #  Format tabel 
    ))


# PROGRAM UTAMA
while True:
    print("\n=== MENU ANIMASI ===")
    print("1. Tampilkan data")
    print("2. Tambah data")
    print("3. Hapus data") 
    print("4. Ubah data")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1-5): ")
    
    if pilihan == "1":
        tampilkan_data()
    elif pilihan == "2":
        tambah_data()
    elif pilihan == "3":
        hapus_data()
    elif pilihan == "4":
        ubah_data()
    elif pilihan == "5":
        print("😇 Jazakumullahukhairan")
        break
    else:
        print("❌ Invalid!")












# Menampilkan data
# Mengubah data
# Menghapus data
# Keluar dari program