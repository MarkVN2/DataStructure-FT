#include <iostream>
#include <string>

//This doesn't use pointers and therefore 
//is incapable of changing the value of the number outside of the function
void changeNumber(int a, int b){
    a = 10;
    b = 15;
}

//This does use pointers and therefore 
//can change the value of the number outside of the function
void changeNumberP(int *a, int *b){
    *a = 10;
    *b = 15;
}

int main(){ 

    int a = 100;
    int b = 500;

    changeNumber(a,b);
    std::cout << a << std::endl; // 100
    std::cout << b << std::endl; // 500

    changeNumberP(&a,&b);
    std::cout << a << std::endl; // 10
    std::cout << b << std::endl; // 15
    
    return 0;
}