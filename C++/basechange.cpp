#include <iostream>
using namespace std;

char lst[] = {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};

int to_base10(int base, char number[]){
    int out = 0;
    for (int i = 0; i < 5; i++){
        int j;
        for (j = 0; j < base; j++){
            if (number[i] == lst[j]){break;}
        }
        out += j;
        out *= base;
    }
    return out;
}

int main(char number[], int base){
    int pr = to_base10(number, base);
    cout << pr << endl;
}

