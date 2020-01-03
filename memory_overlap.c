
#include<stdio.h>


int main()
{
    int N = 1000;
    void *mem1 = malloc(N);
    void *mem2 = malloc(2000);
    char *ptr1 =(char *)mem1;
    char *ptr2 = (char *)mem2;
    printf("\n%x: %x", ptr1, ptr2);
    ptr1 += 500;
    if (ptr1 <= ptr1 + N)
    {
        printf("\nOverlap found!");
    }
    printf("\nincrementing ptr1: %x", ptr1);
}
