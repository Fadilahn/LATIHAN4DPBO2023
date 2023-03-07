// // import library
// #include <iostream>
// #include <string>

// using namespace std;

// #include "Human.cpp"
// #include "SivitasAkademik.cpp"

class Dosen : public SivitasAkademik{
    protected:
        string nip;
        string fakultas;
        string pendTerakhir;
        string keahlian;
    public:
        Dosen(string nik = "", string nama = "", string jenisKelamin = "", string nip = "", string fakultas = "", string pendTerakhir = "", string keahlian = "", string asalUniversitas = "", string emailEdu = "") :
        SivitasAkademik(nik, nama, jenisKelamin, asalUniversitas, emailEdu){
            this->nip = nip;
            this->fakultas = fakultas;
            this->pendTerakhir = pendTerakhir;
            this->keahlian = keahlian;
        }

        string getNip(){return nip;}
        string getFakultas(){return fakultas;}
        string getPendTerahkir(){return pendTerakhir;}
        string getKeahlian(){return keahlian;}

        ~Dosen(){}

};