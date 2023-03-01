class Course:
    # Inisialisasi variabel untuk nama matakuliah
    _nama_matakuliah = ""

    # Konstruktor untuk menginisialisasi variabel nama matakuliah
    def __init__(self, nama_matakuliah=''):
        self._nama_matakuliah = nama_matakuliah

    # Getter untuk mendapatkan nilai nama matakuliah
    def getNamaMatakuliah(self):
        return self._nama_matakuliah