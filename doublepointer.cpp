#include<iostream>

using namespace std;

int main()
{
int **arr;
arr =(int **)malloc(sizeof(int *) * 10);
for ( int i = 0; i < 5; i ++ )
    arr[i] = (int *)malloc(sizeof(int) * 5);

for (int i = 0; i < 5; i++ )
    arr[4][i] = i + 1;

for (int i = 0; i < 5; i++ )
    printf("%d\n",arr[4][i]);

return 0;
}
