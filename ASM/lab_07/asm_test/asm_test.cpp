#include <iostream>

extern "C"
{
    void testAsm();
}

int main() {
    int i;

    __asm {
        mov eax, 5;
        mov i, eax;
    }
    
    std::cout << i;
    testAsm();
    __asm {
        mov i, eax;
    }
    std::cout << i;

    return 0;
}
