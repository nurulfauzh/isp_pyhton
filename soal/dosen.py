from dosen_akademik import DosenAkademik


class Dosen(DosenAkademik):

    def mencatat_kehadiran(self)-> None:
        print ("Dosen mempunyai catatan kehadiran")

    def membuat_ujian(self)-> None:
        print ("Dosen Membuat soal ujian")