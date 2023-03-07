// import library
#include <bits/stdc++.h>

// deklarasi std agar tidak ditulis ulang
using namespace std;

// import kelas kelas yang sudah dibuat
#include "Human.cpp"
#include "SivitasAkademik.cpp"
#include "Mahasiswa.cpp"
#include "Dosen.cpp"
#include "Course.cpp"
#include "ProgramStudi.cpp"

int main() {
    // Membuat objek program studi
    ProgramStudi ilkom("Ilmu Komputer", "IK"), math("Matematika", "M");

    // Menambahkan beberapa objek course ke dalam prodi
    Course course1("Alpro"), course2("Struktur Data"), course3("Aljabar Linear"), course4("Matematika Diskrit");
    ilkom.addCourse(course1);
    ilkom.addCourse(course2);
    math.addCourse(course3);
    math.addCourse(course4);

    // Menambahkan beberapa objek mahasiswa ke dalam prodi
    Mahasiswa
    mhs1("1", "Fadhillah", "Laki-laki", "1", "FPMIPA", "UPI", "F@upi.edu"), 
    mhs2("2", "John Doe", "Laki-laki", "2", "FPMIPA", "UPI", "john.doe@upi.edu"), 
    mhs3("3", "Jane Smith", "Perempuan", "3", "FPMIPA", "UPI", "jane.smith@upi.edu"),
    mhs4("4", "V", "Perempuan", "4", "FPMIPA", "UPI", "V@upi.edu");
    ilkom.addMahasiswa(mhs1);
    ilkom.addMahasiswa(mhs3);
    math.addMahasiswa(mhs2);
    math.addMahasiswa(mhs4);

    // Menambahkan beberapa objek dosen ke dalam prodi
    Dosen 
    dosen1("1", "Prof. X", "Laki-laki", "1", "FPMIPA", "S3", "Kecerdasan Buatan", "UPI", "prof.x@upi.edu"),
    dosen2("2", "Dr. Y", "Perempuan", "2", "FPMIPA", "S2", "Pemrograman Berorientasi Objek", "UPI", "dr.y@upi.edu"),
    dosen3("3", "Dr. Z", "Laki-laki", "3", "FPMIPA", "S2", "Matematika Diskrit", "UPI", "dr.z@upi.edu"),
    dosen4("4", "Prof. W", "Perempuan", "4", "FPMIPA", "S3", "Analisis Real", "UPI", "prof.w@upi.edu");
    ilkom.addDosen(dosen1);
    ilkom.addDosen(dosen2);
    math.addDosen(dosen3);
    math.addDosen(dosen4);

    vector<ProgramStudi> prodiList;

    // Menambahkan objek program studi ke dalam list
    prodiList.push_back(ilkom);
    prodiList.push_back(math);

    // menampilkan data
    for (auto prodi : prodiList) {
        cout << "Program Studi: " << prodi.getNamaProdi() << " (" << prodi.getKode() << ")" << endl;
        cout << "Dosen:" << endl;
        for (auto dosen : prodi.getDosenList()) {
            cout << "- "+dosen.getNama() << endl;
        }

        cout << "Mahasiswa:" << endl;
        for (auto mahasiswa : prodi.getMahasiswaList()) {
            cout << "- "+mahasiswa.getNama() << " (" << mahasiswa.getNim() << ")" << endl;
        }

        cout << "Course:" << endl;
        for (auto course : prodi.getCourseList()) {
            cout << "- "+course.getNamaMatakuliah() << endl;
        }
            cout << endl;
    }

    return 0;
}