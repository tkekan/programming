#include<stdio.h>
#include<stdlib.h>

int main()
{
    int *ptr[10];
    for ( int i = 0 ; i< 10; i++)
        printf("%p\n",ptr[i]);

    for ( int i = 0 ; i < 10; i++)
        ptr[i] = (int *) malloc(sizeof(int));
        
    for ( int i = 0 ; i< 10; i++)
        printf("\nAddress : %p",ptr[i]);
    *ptr[0] = 10;
    int (*p)[10];
    printf("value is  ptr : %d - %p",*ptr[0], ptr[0]);
    return 0;
}
