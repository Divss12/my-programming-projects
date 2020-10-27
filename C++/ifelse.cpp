#include <iostream>
using namespace std;

int main(){
    int number;
    cout << "Enter number: ";
    cin >> number;

    if (number > 0){
        cout << "Number is positive\n";
    }
    else if (number < 0){
        cout << "Number is negative\n";
    }
    else{
        cout << "Number is zero\n";
    }
}