#include <iostream>
using namespace std;
 
int fun(int* ptr)
{   
    *ptr = 40;
    return (*ptr + 10);
}
 
int main(void)
{
    int val = 10;
    int * const cptr = &val;
    *cptr = 40;
    printf(" New value is %d",val);
    int new1 = 20;
    char *cast = (char *) malloc(20*sizeof(char));
    memset(cast,'\0',20);
    cast = reinterpret_cast<char *>(cptr);
    printf("\nPointer address %p - %s",cptr,cast);
    //cptr = const_cast<int *>(&new1);   
    int *ptr =const_cast<int *>(&val);
    printf("\nThe val is %d - %d",*ptr,val);
    printf("\nThe address is %p - %p",ptr,&val);
    int *ptr1 = const_cast <int *>(ptr);
    *ptr = 20;
    //cout << fun(ptr);
    printf("\nThe val is %d - %d",*ptr,val);
    return 0;
}
