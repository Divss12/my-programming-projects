#include <iostream>
#include <cmath>
using namespace std;

float distance(float,float,float,float);

int main(){
    float ax, ay, bx, by;
    cout << "Enter x-coordinate of point 1: ";
    cin >> ax;
    cout << "Enter y-coordinate of point 1: ";
    cin >> ay;
    cout << "Enter x-coordinate of point 2: ";
    cin >> bx;
    cout << "Enter y-coordinate of point 2: ";
    cin >> by;

    float d = distance(ax,ay,bx,by);
    cout << d << endl;
}

float distance(float ax, float ay, float bx, float by){
    float dist = sqrt(pow((ax - bx),2) + pow((ay - by),2));
    return dist;
}