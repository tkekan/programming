
#include<iostream>

using namespace std;

#define enabled 0

typedef union {    
  struct {
    unsigned int code0:4;
    unsigned int code1:4;
    unsigned int code2:4;
  } lbcode;
  unsigned int sumcode;
} lb_hash;

int main()
{
    int j = 10;
    //code C1;
    //unsigned char *p1 = &C1;
    lb_hash code;

    int idx = 0;
    int count = 0x10;
    while (idx < 3) {
        if (idx != 0 ) 
            code.sumcode = code.sumcode << (32 - (4 * idx));
        code.sumcode |= count;
        idx += 1;
        count += 0x1;
    }

    cout << hex << code.lbcode.code0 << endl;
    cout << hex << code.lbcode.code1 << endl; 
    cout << hex << code.lbcode.code2;
    return 0;
        
    }
