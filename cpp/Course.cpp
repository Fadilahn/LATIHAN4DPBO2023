// // import library
// #include <iostream>
// #include <string>

// using namespace std;

class Course{
    protected:
        string namaMatakuliah;
    public:
        Course(string namaMatakuliah = ""){
            this->namaMatakuliah = namaMatakuliah;
        }

        string getNamaMatakuliah(){return namaMatakuliah;}

        ~Course(){}
};