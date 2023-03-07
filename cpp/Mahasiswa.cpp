// import library
// #include <iostream>
// #include <string>

// using namespace std;

// // import class SivitasAkademik
// #include "Human.cpp"
// #include "SivitasAkademik.cpp"

// class Mahasiswa yang merupakan turunan dari class SivitasAkademik
class Mahasiswa : public SivitasAkademik {
    protected:
        string nim;
        string fakultas;

    public:
        // constructor dengan parameter
        Mahasiswa(string nik = "", string nama = "", string jenisKelamin = "", string nim = "", string fakultas = "", string asalUniversitas = "", string emailEdu = "") : 
        SivitasAkademik(nik, nama, jenisKelamin, asalUniversitas, emailEdu){
            this->nim = nim;
            this->fakultas = fakultas;
        }

        string getNim() { return nim; }
        string getFakultas(){return fakultas;}

        // destructor
        ~Mahasiswa(){

        }
};