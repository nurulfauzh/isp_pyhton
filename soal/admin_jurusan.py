from abc import ABC
from kegiatan_akademik import KegiatanAkademik

class AdminJurusan(KegiatanAkademik, ABC):

    def mencatat_kehadiran(self)-> None:
        print("Mencatat kehadiran persemester")
    
    def mempublikasikan_jadwal_ujian(self)-> None:
        print ("mempublikasikan jadwal")

    def membuat_ujian (self) -> None :
        print ("membuat ujian")

    