#include <iostream>
using namespace std;

int main(){
    //Implicit
    int myInt1;
    float myFloat1 = 12.69;
    myInt1 = myFloat1; //.69 at the end will be lost

    //C-Style
    int myInt2;
    float myFloat2 = 69.12;
    myInt2 = (int)myFloat2;

    //Function-Style
    int myInt3;
    float myFloat3 = 33.33;
    myInt3 = int(myFloat3);
    

    char char1 = 'd';
    char char2 = '2';
    int int1 = int(char1);
    int int2 = int(char2);
    cout << char1 << int1 << endl << char2 << int2 << endl;
}