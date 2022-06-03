from kegiatan_akademik import KegiatanAkademik
from abc import ABC, abstractmethod


class DosenAkademik(KegiatanAkademik, ABC) :

    @abstractmethod
    def mencatat_kehadiran(self)-> None:
        pass
    
    @abstractmethod
    def membuat_ujian(self)-> None:
        pass