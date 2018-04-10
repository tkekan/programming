#include <iostream>


using namespace std;

void output_array(int array[][3], int x, int rows, int y, int cols)
{
    if(x > rows || y > rows)
        return;

    else {
        cout << array[x][y];
        output_array(array, x, rows, y+1, cols);
        output_array(array, x+1, rows, y, cols);
    
    }

}

int main()
{

    int array[][3] = {{1,2,3},{4,5,6}};

    output_array(array,0,1,0,1);


}
