#include <iostream>
#include <map>
#include <unordered_set>

using namespace std;
int main()
{

    map <char,char> mymap = {{'1','1'},{'8','8'}, {'6','9'}};
    unordered_set <pair<int,int>> myset;
    pair <int,int> mypair = make_pair(1,2);
    //myset.insert(x);
    for (auto it: mymap)
    {
        cout << it.first << ":" << it.second << endl;
    }

return 0;
}
