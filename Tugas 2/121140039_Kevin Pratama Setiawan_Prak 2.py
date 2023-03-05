#Soal 1
class Orang :
    jumlah_tangan = 2
    jumlah_kaki = 2

    def __init__(self, nama, pekerjaan, tahun_lahir) :
        self.nama = nama
        self.pekerjaan = pekerjaan
        self.tahun_lahir = tahun_lahir

    def berjalan_kedepan(self):
        print("melangkah")
        print("posisi berpindah")

orang1 = Orang("Enrico", "Mahasiswa", 2000)
orang2 = Orang("Andi", "Direktur", 1980)
print(orang1.nama)
print(orang1.pekerjaan)
print(orang2.nama)
print(orang2.pekerjaan)
print(orang1.jumlah_kaki)
print(orang2.jumlah_kaki)
orang1.berjalan_kedepan()

#Soal 2
class Saya :
    def __init__ (self, nama, nim, kelas, jml_sks):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.jml_sks = jml_sks

    def mengambil_sks (self, tambah):
        self.jml_sks += tambah
        print(f"Jumlah SKS {self.nama} menjadi {self.jml_sks}")

    

Saya1 = Saya("Kevin", "121140039", "RB", 3)
Saya1.mengambil_sks(3)
