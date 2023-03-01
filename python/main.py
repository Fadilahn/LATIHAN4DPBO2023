#Import kelas yang diperlukan 
from Mahasiswa import Mahasiswa
from Dosen import Dosen
from Course import Course
from ProgramStudi import ProgramStudi

# create instances of Course
course = Course("DPBO")
course2 = Course("Big Data")
math = Course("Matematika")

# create instances of ProgramStudi and add courses to them
prodi = ProgramStudi("Ilmu Komputer", "IK")
prodi.addCourse(course)
prodi.addCourse(course2)

prodi2 = ProgramStudi("Pendidikan Matematika", "PM")
prodi2.addCourse(math)

# create instances of Mahasiswa and Dosen
mahasiswa = Mahasiswa("1", "Fadhillah", "Male", "1", "FPMIPA", prodi, "UPI", "F@upi.edu")
mahasiswa.addCourse(course)
mahasiswa.addCourse(course2)

mahasiswa2 = Mahasiswa("2", "V", "Female", "2", "FPMIPA", prodi2, "UPI", "V@upi.edu")
mahasiswa2.addCourse(math)

dosen = Dosen("2", "Rosa", "Female", "2", "FPMIPA", prodi, "S3", "Programing", "UPI", "R@upi.edu")
dosen.addCourse(course)

# print data for mahasiswa1
# mahasiswa.displayInfo()
print("Data mahasiswa:")
print("NIK:", mahasiswa.getNik())
print("Nama:", mahasiswa.getNama())
print("Jenis Kelamin:", mahasiswa.getJenisKelamin())
print("NIM:", mahasiswa.getNim())
print("Fakultas:", mahasiswa.getFakultas())
print("Program Studi:", mahasiswa.getProdi().getNamaProdi())
print("Kode Program Studi:", mahasiswa.getProdi().getKode())
print("Course:")
for course in mahasiswa.getCourse():
    print("-", course.getNamaMatakuliah())
print("Asal Universitas:", mahasiswa.getAsalUniversitas())
print("Email Edu:", mahasiswa.getEmailEdu())

# print data for dosen
print("\nData dosen:")
print("NIK:", dosen.getNik())
print("Nama:", dosen.getNama())
print("Jenis Kelamin:", dosen.getJenisKelamin())
print("NIP:", dosen.getNip())
print("Fakultas:", dosen.getFakultas())
print("Program Studi:", dosen.getProdi().getNamaProdi())
print("Kode Program Studi:", dosen.getProdi().getKode())
print("Course:", dosen._courses[0].getNamaMatakuliah())
print("Pendidikan Terakhir:", dosen.getPendTerakhir())
print("Keahlian:", dosen.getKeahlian())
print("Asal Universitas:", dosen.getAsalUniversitas())
print("Email Edu:", dosen.getEmailEdu())
