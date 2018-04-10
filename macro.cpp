
#include<iostream>

#define square(x) ((x) * (x))

using namespace std;
int main()
{
    int i = 5;
    int j = square(i++);
    printf("Val : %d",j);
    return 0;
}
