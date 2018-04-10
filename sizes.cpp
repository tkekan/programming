#include<iostream>

using namespace std;

int main()
{
    unsigned char two;
    unsigned char sample = 127;
    //unsigned char *three =(unsigned char) &sample;
    for ( int i =0 ; i < 255; i++) {
        printf("char is %d : %c\n",i,i);
        int ch = cin.get();
    } 
    return 0;
    
}
