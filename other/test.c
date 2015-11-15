#include<stdio.h>
int main()
{
    int a= 10;
    int b = 2;
    b = a++ + a++ + a++;
    printf("a=%d, b=%d", a, b);
    return 0;
}
