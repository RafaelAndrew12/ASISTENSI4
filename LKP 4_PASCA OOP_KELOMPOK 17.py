# Class Inheritance
class orang:
    def __init__ (self, nama, asal):
        self.nama = nama
        self.asal = asal
    def perkenalan(self):
        return (f"Perkenalkan saya {self.nama} dari {self.asal}")

class mahasiswa (orang):
    def __init__(self, nama, asal, universitas, programstudi, angkatan):
        super().__init__(nama, asal)
        self.universitas = universitas
        self.programstudi = programstudi
        self.angkatan = angkatan
    def perkenalan(self):
        return (f"Perkenalkan saya {self.nama} dari {self.asal} mahasiswa {self.universitas} programstudi {self.programstudi} angkatan {self.angkatan}")

Ulayya = orang("Ulayya","Sidoarjo\n")
print(Ulayya.perkenalan())
Iklilia = mahasiswa("Iklilia","Bekasi","Universitas Brawijaya","Teknik Industri","2021\n")
print(Iklilia.perkenalan())
# Shafa = orang("Shafa","Sidoarjo\n")
# print(Shafa.perkenalan())
# Gilang = mahasiswa("Gilang","Lumajang","Universitas Brawijaya","Teknik Industri","2021\n")
# print(Gilang.perkenalan())
# Virgy = orang("Virgy","Surabaya\n")
# print(Virgy.perkenalan())
# Rafael = mahasiswa("Rafael", "Malang","Universitas Brawijaya","Teknik Industri","2021")
# print(Rafael.perkenalan())