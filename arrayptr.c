
#include<stdio.h>

void swap(int *, int *);

void swap(int *x, int *y)
{
    printf("\nIn swap : x : %d, y = %d\n",*x,*y);
    int temp = *x;
    *x = *y;
    *y = temp;
}
int main()
{
    int arr[] = {1,2,3};
    int *a = arr;
    swap(&a[0],&a[2]);

    for ( int i = 0; i < 3; i++)
        printf("%d\n",a[i]);
    char ch = 'b';
    printf("\n\n%d\n",(int)ch - 97);
    return 0;
}
