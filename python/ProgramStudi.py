class ProgramStudi:
    # Inisialisasi variabel untuk nama program studi, kode program studi, dan daftar matakuliah
    _nama_prodi = ""
    _kode = ""
    _courses = []

    # Konstruktor untuk menginisialisasi variabel nama program studi dan kode program studi
    def __init__(self, nama_prodi='', kode=''):
        self._nama_prodi = nama_prodi
        self._kode = kode

    # Method untuk menambahkan matakuliah pada daftar matakuliah program studi
    def addCourse(self, course):
        self._courses.append(course)

    # Method untuk menghapus matakuliah dari daftar matakuliah program studi
    def deleteCourse(self, course):
        self._courses.remove(course)

    # Getter untuk mendapatkan daftar matakuliah program studi
    def getCourses(self):
        return self._courses

    # Getter untuk mendapatkan nama program studi
    def getNamaProdi(self):
        return self._nama_prodi

    # Getter untuk mendapatkan kode program studi
    def getKode(self):
        return self._kode   