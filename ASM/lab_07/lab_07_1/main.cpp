﻿#include <iostream>
#include <cstring>

using namespace std;

extern "C" 
{
    void myStrcpy(char* dst, const char* src, int len);
}

size_t my_strlen(const char* str) 
{
    size_t result = 0;
    while (*(str++) != 0)
        result++;
    return result;
}

size_t asm_strlen(const char* str) {
    size_t len = 0;
    __asm {
            push ecx
            push edi
            mov ecx, -1
            mov edi, str
            xor al, al
            repne scasb
        not ecx
            dec ecx
            mov len, ecx
            pop edi
            pop ecx
    }
    return len;
}

int main()
{
    char str[100] = "Test strlen for lab_07 assambler!";
    printf("Test string: %s\n", str);
    int l = asm_strlen(str);
    cout << "asm_strlen: " << l << endl;
    l = my_strlen(str);
    cout << "my_strlen: " << l << endl;
    l = strlen(str);
    cout << "strlen: " << l << endl;

    char src[] = "test strcpy for lab_07 asm";
    char dst[] = "test strcpy for lab_07 asm";
    int len = asm_strlen(src);

    printf("Test string: %s\n", src);
    myStrcpy(dst, src, len);
    printf("Identic strings: %s\n", dst);

    char before[100] = { '0' },
        * middle = before + 2,
        * after = middle + 2;

    printf("String length = %d\n", len);

    myStrcpy(middle, src, len);
    printf("Coppied string: %s\n", middle);

    myStrcpy(before, middle, len);
    printf("Copy before pointer: %s\n", before);

    myStrcpy(after, before, len);
    printf("Copy after pointer: %s\n", before);


    return 0;
}
