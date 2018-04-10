#include <stdio.h>
 
int main(void)
{
    const int local = 10;
    int *ptr = &local;
 
    printf("Initial value of local : %d - %p \n", local, &local);
 
    *ptr = 100;
 
    printf("Modified value of local: %d  *ptr: %d  ptr: %p \n", local, *ptr, ptr);
 
    return 0;
}
