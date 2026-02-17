
data_santri = []
data_perizinan = []

def simpan_data():
    with open('data.txt', 'w', encoding='utf-8') as f:  
        f.write("SANTRI\n")
        for s in data_santri:
            f.write(f"{s['nama']},{s['kamar']}\n")
        f.write("\nPERIZINAN\n")
        for p in data_perizinan:
            f.write(f"{p.get('no_izin', 'N/A')},{p.get('nama', 'N/A')},"
                   f"{p.get('kamar', 'N/A')},{p.get('hari', 'N/A')},"
                   f"{p.get('tanggal', 'N/A')},{p.get('jam', 'N/A')},"
                   f"{p.get('status', 'pending').replace('❌', 'X')},"  
                   f"{p.get('musyrif_Pengizin', '')},{p.get('komentar_musyrif', '')}\n")
    print("💾 Data tersimpan!")



def load_data():
    global data_santri, data_perizinan
    data_santri.clear()
    data_perizinan.clear()
    try:
        with open('data.txt', 'r') as f:
            lines = f.readlines()
            mode = ""
            for line in lines:
                line = line.strip()
                if line == "SANTRI":
                    mode = "santri"
                elif line == "PERIZINAN":
                    mode = "perizinan"
                elif ',' in line and mode:
                    parts = line.split(',')
                    if mode == "santri":
                        data_santri.append({'nama': parts[0], 'kamar': parts[1]})
                    else:
                        data_perizinan.append({
                            'no_izin': parts[0], 'nama': parts[1], 'kamar': parts[2],
                            'tanggal': parts[3], 'jam': parts[4], 'status': parts[5],
                            'musyrif_Pengizin': parts[6] if len(parts)>6 else ''
                        })
    except FileNotFoundError:
        pass  # File belum ada

# Auto load saat import
load_data()
