#include <iostream>
using namespace std;

int main(){
    //First, WHILE loop:
    int i = 0;
    while (i<100) {
        if (i%3 == 0){
            cout << "Fizz";
        }

        if (i%5 == 0){
            cout << "Buzz"; 
        }
        else if (i%3 != 0){
            cout << i;
        }
        cout << endl;
        i++;
    }

    //Next, DO WHILE loop:

    float number, sum = 0.0;
    do {
        cout << "Enter a number: ";
        cin >> number;
        sum += number;
    }
    while (number != 0.0);

    cout<<"Total sum = "<<sum;

    return 0; //The difference is, the do while loop runs its code once before checking the condition
}