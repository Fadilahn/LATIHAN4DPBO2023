// // import library
// #include <iostream>
// #include <string>

// using namespace std; //menggunakan namespace std

// #include "Human.cpp" //mengimpor file Human.cpp

class SivitasAkademik : public Human { //membuat kelas SivitasAkademik yang merupakan turunan dari kelas Mahasiswa
    protected: //mendefinisikan akses proteksi
        string asalUniversitas; //mendeklarasikan variabel asalUniversitas bertipe string
        string emailEdu; //mendeklarasikan variabel emailEdu bertipe string

    public: //mendefinisikan akses publik

        SivitasAkademik(string nik = "", string nama = "", string jenisKelamin = "", string asalUniversitas = "", string emailEdu = "") : 
        Human(nik, nama, jenisKelamin){ //mendefinisikan konstruktor dengan parameter untuk kelas SivitasAkademik yang juga memanggil konstruktor dengan parameter dari kelas Mahasiswa
            this->asalUniversitas = asalUniversitas; //menginisialisasi variabel asalUniversitas dengan nilai yang diterima melalui parameter
            this->emailEdu = emailEdu; //menginisialisasi variabel emailEdu dengan nilai yang diterima melalui parameter
        }

        string getAsalUniversitas(){return asalUniversitas;}
        string getEmailEdu(){return emailEdu;}

        ~SivitasAkademik(){} //mendefinisikan destruktor untuk kelas SivitasAkademik
};