from interface.penolakan_operation import PenolakanOperation
from abc import ABC, abstractmethod

class PenjualOperation(PenolakanOperation, ABC):

    @abstractmethod
    def menolak_pesanan (self) -> None :
        super().menolak_pesanan()

    @abstractmethod
    def menyiapkan_pesanan (self) -> None :
        pass