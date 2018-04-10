#include<iostream>
#include "bitwise.h"
using namespace std;


void addnumber(int num)
{
    int mask = 0x1;
    int count = 0;
    printf("\nsize is : %lu",sizeof(int *));
    for ( int i = 0; i < sizeof(int *); i++) {
        if ( mask & num ) {
            count+=1; 
            mask = mask << 1;
            continue;
        }
        else 
            break;
    }
    printf("\nBit set till %d", count);
    mask = 0x0;
    for ( int j = 0; j < count; j++ ) {
        mask = (mask << 1) | 1;
    }
    int newnum = num & ~(mask);
    newnum = newnum | ( 1 << count );
    printf("\nNew number is %d",newnum);
}


void power()
{
    int num = 1;
    while (true)
    {   
        num = num << 1;
        printf("left shift %d", num);
        cin.get();
    }    
    
}
int main()
{
    int value = 0x11111111;
    int *bit = &value;
    int mask = 0x1;
    unsigned char *ptr = (unsigned char *)bit;
    for ( int i = 0 ; i < sizeof(bit); i++)
    {
        if ( (*ptr) & mask)
            printf("\n%d bit set",i);
        printf("\naddress : %p",ptr);
        ptr++;
    }

    //Add number to an integer
    addnumber(-16);
    power();
    return 0;
}
