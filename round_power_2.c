
#include<stdio.h>


unsigned int round2(unsigned int v)
{
    v--;
     v |= v >> 1;
    v |= v >> 2;
    v |= v >> 4;
    v |= v >> 8;
    v |= v >> 16;
    v++;
    return v;
}

int main()
{
    int v = 250;
    printf("\n%u", round2(v + (v >> 2)));
}
