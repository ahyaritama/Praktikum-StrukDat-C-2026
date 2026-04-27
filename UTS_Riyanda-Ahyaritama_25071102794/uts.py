pengunjung_hari_ini = [
    {"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi", "kembali": False},
    {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains", "kembali": True},
    {"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi", "kembali": False},
    {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum", "kembali": True},
    {"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains", "kembali": False},
    {"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum", "kembali": False},
]

def tampilkan_pengunjung(data):
    print("===== DATA PENGUNJUNG PERPUSTAKAAN =====")
    print("No | ID | Nama | Usia | Kategori | Status Kembali")
    print("---+------+--------+------+----------+---------------")

    for i in range(len(data)):
        print(f"{i + 1}  | {data[i]["id"]} | {data[i]["nama"]} | {data[i]["usia"]} | {data[i]["kategori"]} | {"Sudah Kembali" if data[i]["kembali"] else "Belum Kembali"}")
    
    print()

def filter_belum_kembali(data):
    belum_kembali = [x["nama"] for x in data if x["kembali"] == False]
    belum_kembali.sort()

    print("===== PENGUNJUNG BELUM KEMBALI =====")
    for i in range(len(belum_kembali)):
        print(f"{i + 1}. {belum_kembali[i]}")
    print(f"Total belum kembali: {len(belum_kembali)} pengunjung")
    print()

    


tampilkan_pengunjung(pengunjung_hari_ini)
filter_belum_kembali(pengunjung_hari_ini)


def info_perpustakaan(data):
    informasi_perpustakaan = ("Perpustakaan Kampus Terpadu", "Jl. Pendidikan No. 5, Pekanbaru", "0761-54321")
    buku_unik = {x["kategori"] for x in data}


    print("Info Perpustakaan:")
    print("Nama :", informasi_perpustakaan[0])
    print("Alamat :", informasi_perpustakaan[1])
    print("Telp :", informasi_perpustakaan[2])
    print()

    print("Kategori Buku Unik:", buku_unik)
    print("Jumlah kategori:", len(buku_unik))
    print()



def rekap_kategori(data):
    buku_unik = {x["kategori"] for x in data}
    pengunjung = {}
    for x in buku_unik:
        banyak = 0
        for y in data:
            if y["kategori"] == x:
                banyak += 1
        pengunjung[x] = banyak

    print("Rekap per kategori:")
    for x, y in pengunjung.items():
        print(f"{x} : {y} pengunjung")
    print()
    
    terbanyak = []
    max = 0
    for x, y in pengunjung.items():
        if y > max:
            terbanyak = [x]
            max = y
        elif y == max:
            terbanyak.append(x)
    
    print(f"Kategori terbanyak: {str.join(", ", terbanyak)} ({max} Pengunjung)")

    print()


info_perpustakaan(pengunjung_hari_ini)
rekap_kategori(pengunjung_hari_ini)


class Pengunjung:
    total = 0

    def __init__(self, id, nama, kategori):
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori
        Pengunjung.total += 1

    def get_id(self):
        return self.__id
    
    def get_nama(self):
        return self.__nama

    def get_kategori(self):
        return self.__kategori
    
    def tampilkan_info(self):
        print("ID       :", self.__id)
        print("Nama     :", self.__nama)
        print("Kategori :", self.__kategori)
        print()
    
    @staticmethod
    def hitung_pengunjung():
        print("Total pengunjung terdaftar:", Pengunjung.total)
        print()


class PengunjungPrioritas(Pengunjung):
    def __init__(self, id, nama, kategori, prioritas):
        super().__init__(id, nama, kategori)
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori
        self.prioritas = "Mendesak" if prioritas else "Biasa"
    
    def tampilkan_info(self):
        print("ID        :", self.__id)
        print("Nama      :", self.__nama)
        print("Kategori  :", self.__kategori)
        print(f"Prioritas : {self.prioritas}{"\n** Layani segera! **" if self.prioritas == "Mendesak" else ""}")
        print()

p1 = Pengunjung("M001", "Rina", "Fiksi")
p2 = PengunjungPrioritas("M007", "Gilang", "Referensi", True)

p1.tampilkan_info()
p2.tampilkan_info()
Pengunjung.hitung_pengunjung()


class Node:
    def __init__(self, data: dict):
        self.data = data
        self.next = None

class AntrianPeminjaman:
    def __init__(self, head: Node):
        self.head = head
    
    def tambah(self, data):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        
        current_node.next = Node(data)

    def tampilkan(self):
        print("===== ANTRIAN PEMINJAMAN =====")
        current_node = self.head
        counter = 1
        while current_node:
            print(f"[{counter}] {current_node.data["id"]} - {current_node.data["nama"]} | {current_node.data["kategori"]}")
            current_node = current_node.next
            counter += 1

        print()

    def panggil_berikutnya(self):
        print("Memanggil pengunjung berikutnya...")
        if self.head.next:
            print(f"Silahkan masuk: {self.head.data["nama"]} ({self.head.data["id"]}) - {self.head.data["kategori"]}\n")
            self.head = self.head.next
        else:
            print("Pengunjung Sudah Habis")

    def cari(self, nama: str):
        current_node = self.head
        counter = 1
        while current_node:
            if current_node.data["nama"] == nama:
                print(f"Ditemukan: {current_node.data["id"]} - {current_node.data["nama"]} | {current_node.data["kategori"]} (posisi ke-{counter})")
                return
            else:
                counter += 1
                current_node = current_node.next
        print("Tidak ditemukan")


    def hapus_berdasarkan_id(self, id):
        print(f"Menghapus pengunjung dengan ID {id}...")
        if self.head.data["id"] == id:
            self.head = self.head.next
            return
        
        current_node = self.head
        while current_node.next:
            if current_node.next.data["id"] == id:
                print(f"{current_node.next.data["nama"]} ({current_node.next.data["id"]}) berhasil dihapus dari antrian.\n")
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
        
        print(f"Pengunjung dengan ID {id} tidak ditemukan.\n")


    def hitung(self):
        current_node = self.head
        counter = 0
        while current_node:
            counter += 1
            current_node = current_node.next
        return counter


antrian = AntrianPeminjaman(Node({"id": "M001", "nama": "Rina", "kategori": "Fiksi"}))
antrian.tambah({"id": "M002", "nama": "Hendra", "kategori": "Sains"})
antrian.tambah({"id": "M003", "nama": "Siti", "kategori": "Fiksi"})
antrian.tambah({"id": "M004", "nama": "Taufik", "kategori": "Hukum"})
antrian.tampilkan()
antrian.panggil_berikutnya()
antrian.tampilkan()
print("Total antrian:", antrian.hitung())
antrian.hapus_berdasarkan_id("M003")
antrian.tampilkan()
antrian.cari("Taufik")
print("Total antrian:", antrian.hitung())