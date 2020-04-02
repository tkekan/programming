
#include<stdio.h>
#include <time.h>


union s {
    struct {
        int code0:4;
        int code1:4;
        int code2:4;
    }lb; 
   int total;
};

union cars {
    char s1[20];
    char s2[30];
    short int s3;
};

int main()
{
const struct timespec ns = {0,999999};
    union cars c1;
    printf("size: %d", sizeof(c1));

union s s1;
s1.lb.code0 = 1;
s1.lb.code1 = 2;
printf ("total: %d", s1.total);
}
