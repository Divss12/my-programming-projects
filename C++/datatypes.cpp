#include <iostream>
using namespace std;

//These are the main datatypes in C++

int main(){
    int integer = 12; //stores an integer
    //decimal by defualt, octal starts with 0 and hexadecimal with 0x
    int octal = 014;
    int hexadecimal = 0xC;

    float number = 12.12; //stores a floating point number
    double number = 12.12; //stores a floating point number with double the bytes
    float exponent = 12E12; //stores a number in exponential form (12E12  =  12 * 10^12)

    char letter = 'd'; //stores just one character

    bool condition = true; //stores a Boolean value

    //void is another datatype which means the absence of a value. It is not possible to declare a variable of this datatype

    /*
    TYPE MODIFIERS
    */

   // There are four modifiers: signed, unsigned, short and long
   // These can be applied to the basic datatypes: int, double and char
   // signed allows for negative and positive values
   // unsigned allows only positive values, but allows values to be twice as large
   // short allows only shorter values
   // long allows longer values; long long allows even larger values

   return 0;
}