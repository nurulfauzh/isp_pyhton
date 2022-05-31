from interface.penjual_operation import PenjualOperation

class penjualancontroller(PenjualOperation):

    def menolak_pesanan(self) -> None:
        print("penjual menolak pesanan karena stok habis")

    def menyiapkan_pesanan(self) -> None:
        print("penjual menyiapkan pesannan sesuai pilihan pembeli")
        