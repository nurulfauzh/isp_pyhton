from abc import ABC, abstractmethod

class KegiatanAkademik(ABC):
 
    @abstractmethod
    def mencatat_kehadiran(self)-> None:
        pass

    @abstractmethod
    def mengerjakan_ujian(self) -> None :
        pass
    
    @abstractmethod
    def membuat_ujian(self) -> None :
        pass

    @abstractmethod
    def mempublikasikan_jadwal_ujian(self)-> None:
        pass