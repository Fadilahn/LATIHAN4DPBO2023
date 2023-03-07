// // import library
// #include <iostream>
// #include <string>
// #include <vector>

// using namespace std;

// #include "Human.cpp"
// #include "SivitasAkademik.cpp"
// #include "Mahasiswa.cpp"
// #include "Dosen.cpp"
// #include "Course.cpp"

class ProgramStudi{
    protected:
        string namaProdi;
        string kode;
        vector<Course> course;
        vector<Mahasiswa> mahasiswa;
        vector<Dosen> dosen;

    public:
        ProgramStudi(string namaProdi = "", string kode = ""){
            this->namaProdi = namaProdi;
            this->kode = kode;
        }

        void addCourse(Course course = Course()){
            this->course.push_back(course);
        }

        void addMahasiswa(Mahasiswa mahasiswa = Mahasiswa()){
            this->mahasiswa.push_back(mahasiswa);
        }

        void addDosen(Dosen dosen = Dosen()){
            this->dosen.push_back(dosen);
        }

        vector<Course> getCourseList(){
            return course;
        }

        vector<Mahasiswa> getMahasiswaList(){
            return mahasiswa;
        }

        vector<Dosen> getDosenList(){
            return dosen;
        }

        string getNamaProdi(){return namaProdi;}
        string getKode(){return kode;}

        ~ProgramStudi(){}
};