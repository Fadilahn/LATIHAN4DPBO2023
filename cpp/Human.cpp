// // import library
// #include <iostream>
// #include <string>

// // deklarasi std agar tidak ditulis ulang
// using namespace std;

// kelas dasar Human, untuk merepresentasikan manusia
class Human {
    // variabel-variabel yang hanya dapat diakses oleh kelas turunan
    protected:
        string nik;
        string nama;
        string jenisKelamin;

    public:

        // konstruktor dengan parameter
        Human(string nik = "", string nama = "", string jenisKelamin = "") {
            this->nik = nik;
            this->nama = nama;
            this->jenisKelamin = jenisKelamin;
        }

        string getNik(){return nik;}
        string getNama(){return nama;}
        string getJenisKelamin(){return jenisKelamin;}

        // destruktor kosong
        ~Human(){

        }
};