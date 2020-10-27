#include <iostream>
using namespace std;

int main(){
    int i;
    cout << "Enter a number: ";
    cin >> i;
    switch(i){
        case 1:
            cout << "one\n";
            break;
        case 2:
            cout << "two\n";
            break;
        case 3:
            cout << "three\n";
            break;
        default:
            cout << "greater than 3\n";
            break;
    }
}
//switch executes all code after first statement that is true
