class Human:
    # Inisialisasi variabel untuk NIK, nama, dan jenis kelamin
    _nik = ""
    _nama = ""
    _jenis_kelamin = ""

    # Konstruktor untuk menginisialisasi variabel NIK, nama, dan jenis kelamin
    def __init__(self, nik='', nama='', jenis_kelamin=''):
        self._nik = nik
        self._nama = nama
        self._jenis_kelamin = jenis_kelamin

    # Getter untuk mendapatkan nilai NIK
    def getNik(self):
        return self._nik

    # Getter untuk mendapatkan nilai nama
    def getNama(self):
        return self._nama

    # Getter untuk mendapatkan nilai jenis kelamin
    def getJenisKelamin(self):
        return self._jenis_kelamin