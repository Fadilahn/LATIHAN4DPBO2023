from Human import Human

class SivitasAkademik(Human):
    # Inisialisasi variabel untuk asal universitas dan email edu
    _asal_universitas = ""
    _email_edu = ""

    # Konstruktor untuk menginisialisasi variabel NIK, nama, jenis kelamin, asal universitas, dan email edu
    def __init__(self, nik='', nama='', jenis_kelamin='', asal_universitas='', email_edu=''):
        super().__init__(nik, nama, jenis_kelamin)
        self._asal_universitas = asal_universitas
        self._email_edu = email_edu

    # Getter untuk mendapatkan nilai asal universitas
    def getAsalUniversitas(self):
        return self._asal_universitas

    # Getter untuk mendapatkan nilai email edu
    def getEmailEdu(self):
        return self._email_edu