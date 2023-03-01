from SivitasAkademik import SivitasAkademik
from ProgramStudi import ProgramStudi

# Membuat class Dosen yang merupakan turunan dari class SivitasAkademik
class Dosen(SivitasAkademik):
    # Inisiasi atribut _nip, _fakultas, _prodi, _course, _pend_terakhir dan _keahlian
    _nip = ""
    _fakultas = ""
    _prodi = ProgramStudi()
    _courses = []
    _pend_terakhir = ""
    _keahlian = ""

    # Method constructor yang akan dijalankan ketika class Dosen dipanggil
    def __init__(self, nik='', nama='', jenis_kelamin='', nip='', fakultas='', prodi='', pend_terakhir='', keahlian='', asal_universitas='', email_edu=''):
        # Memanggil constructor dari class induk SivitasAkademik
        super().__init__(nik, nama, jenis_kelamin, asal_universitas, email_edu)
        # Mengisi nilai atribut _nip dengan nilai yang diinputkan
        self._nip = nip
        # Mengisi nilai atribut _fakultas dengan nilai yang diinputkan
        self._fakultas = fakultas
        # Mengisi nilai atribut _prodi dengan nilai yang diinputkan
        self._prodi = prodi
        # Mengisi nilai atribut _pend_terakhir dengan nilai yang diinputkan
        self._pend_terakhir = pend_terakhir
        # Mengisi nilai atribut _keahlian dengan nilai yang diinputkan
        self._keahlian = keahlian

    def addCourse(self, course):
        self._courses.append(course)

    def getNip(self):
        return self._nip

    def getFakultas(self):
        return self._fakultas

    def getProdi(self):
        return self._prodi
    
    def getCourse(self):
        return self._courses

    def getPendTerakhir(self):
        return self._pend_terakhir

    def getKeahlian(self):
        return self._keahlian