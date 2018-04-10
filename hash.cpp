#include<iostream>
#include <unordered_map>
#include<vector>

using namespace std;

unordered_map< string, vector<int> >mymap;


int main()
{
    vector<int>values;
    values.push_back(10);
    values.push_back(20);
    mymap["tanvir"] = values;
    mymap["tanvir"].push_back(30);
    for (auto& i: mymap["tanvir"])
        cout<<i;
    unordered_map< string, vector<int> >::const_iterator got = mymap.find("tanvir");
    if (got == mymap.end() )
        cout << "what!!";
    return 0;
}
