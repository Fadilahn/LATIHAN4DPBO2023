from SivitasAkademik import SivitasAkademik
from ProgramStudi import ProgramStudi

# Membuat class Mahasiswa yang merupakan turunan dari class SivitasAkademik
class Mahasiswa(SivitasAkademik):
    # Inisiasi atribut _nim, _fakultas, _prodi dan _course
    _nim = ""
    _fakultas = ""
    _prodi = ProgramStudi()
    _courses = []
    
    # Method constructor yang akan dijalankan ketika class Mahasiswa dipanggil
    def __init__(self, nik='', nama='', jenis_kelamin='', nim='', fakultas='', prodi='', asal_universitas='', email_edu=''):
        # Memanggil constructor dari class induk SivitasAkademik
        super().__init__(nik, nama, jenis_kelamin, asal_universitas, email_edu)
        # Mengisi nilai atribut _nim dengan nilai yang diinputkan
        self._nim = nim
        # Mengisi nilai atribut _fakultas dengan nilai yang diinputkan
        self._fakultas = fakultas
        # Mengisi nilai atribut _prodi dengan nilai yang diinputkan
        self._prodi = prodi

    def addCourse(self, course):
        self._courses.append(course)

    # Method untuk mengembalikan nilai atribut _nim
    def getNim(self):
        return self._nim

    # Method untuk mengembalikan nilai atribut _fakultas
    def getFakultas(self):
        return self._fakultas

    # Method untuk mengembalikan nilai atribut _prodi
    def getProdi(self):
        return self._prodi
    
    def getCourse(self):
        return self._courses
    
    def displayInfo(self):
        print("NIM:", self._nim)
        print("Nama:", self._nama)
        print("Jenis Kelamin:", self._jenis_kelamin)
        print("Fakultas:", self._fakultas)
        print("Prodi:", self._prodi.getNamaProdi())
        print("Course:")
        for i in self._courses:
            print("-", i.getNamaMatakuliah())
        print("Universitas:", self._asal_universitas)
        print("Email:", self._email_edu)