from interface.penolakan_operation import PenolakanOperation
from abc import ABC, abstractmethod 

class DriverOperation (PenolakanOperation, ABC) :

    @abstractmethod
    def menolak_pesanan(self) -> None :
        pass

    @abstractmethod
    def mengantarkan_pesanan(self) -> None :
        pass