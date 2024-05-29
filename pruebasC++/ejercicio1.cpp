
#include <iostream>  
#include <vector>

union U1 
{
    int a;
    int b;
};

union U2
{
    U1   u;
    int  i;
};

int main() {
    U1 u1{10};
    U2 u2{u1};
    u2.u.a = 100;
    std::cout << u2.i << ", " << u2.u.a << ", "<< u1.b;
}
