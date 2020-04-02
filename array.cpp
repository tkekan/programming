#include<iostream>


using namespace std;

int main()
{
    int array[] = {5,5,0,1,2,3,4,5};
    int r =  sizeof(array)/sizeof(array[0]);
    int l = 0;
    r = r - 1;
    int target = -1;
    while (l <= r) {
        int mid = (l+r)/2;
        if (array[mid] == target) {
            cout <<"Found";
            return true;
        }
        if (array[l] < array[mid]) {
            if (target > array[l] && target < array[mid])
                r = mid - 1;
            else
                l = mid + 1;
        } else if(array[l] > array[mid]) {
            if (target > array[mid] && target <= array[r])
                l = mid + 1;
            else
                r = mid - 1;
        }
          else {
                l += 1;
          }
    }
    cout << "Not found";
    return 0;

}
