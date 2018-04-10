
#include<stdio.h>

typedef struct Node
{
    int data;
    struct Node *left;
    struct Node *right;
}NODE;
int main()
{
    int i, j;
    int **arr;
    NODE *root;
    arr =  (int **)malloc(4 * sizeof(int *));
    arr[0] = (int *)malloc(sizeof(int) * 4 * 4);
    /*
    for ( i =0 ; i < 4; i++)
        arr[i] = (int *)malloc( 4 * sizeof(int));
    
    for ( i =0 ; i< 4; i++)
    {
        arr[i] =(int *)malloc(4 * sizeof(int));    
    }
*/
    int count = 0;
    for ( i=0 ; i< 4; i++) {
        for ( j= 0 ; j < 4; j ++) {
            arr[i][j]  = ++count;
        }
    }


    for ( i=0 ; i< 4; i++) {
        for ( j= 0 ; j < 4; j ++) {
            printf(" %d ", arr[i][j]);
        }
    }

}
