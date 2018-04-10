#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main ()
{
   vector<int> vec (4); 
  vec[0] = 10;
  vec[1] = 1;
  vec[2] = 2;
  vec[3] = 20;
    

    priority_queue<int, vector<int>, greater<int> > pq; //= get_k_clostest_points(vec, 2);
        for(int i = 0 ; i< 4 ; i++ )
        {
            pq.push(vec[i]);
        
        }
        while(!pq.empty()) {
                    cout << pq.top() << ' ';
                            pq.pop();
                                }
            
            return 0;
}
