#include<stdio.h>


int main()
{
    int mask = 0x1;
    int num = -10;
    int count = 0;
    while (num) {
        if (num & mask)
            count += 1;
        num = num >> 1;
    }
    printf("Total number of bits: %d",count);
}
