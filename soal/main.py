from admin_jurusan import AdminJurusan
from dosen import Dosen
from mahasiswa import Mahasiswa

AdminJurusan1 = AdminJurusan()
print (AdminJurusan1.membuat_ujian())
print (AdminJurusan1.mempublikasikan_jadwal_ujian())
print (AdminJurusan1.mencatat_kehadiran())

dosen1 = Dosen()
print (dosen1.mencatat_kehadiran())
print (dosen1.membuat_ujian())

mahasiswa = Mahasiswa()
print (mahasiswa.mengerjakan_ujian())
print (mahasiswa.mencatat_kehadiran())
