#include<iostream>
#include<vector>
#include <algorithm> 

using namespace std;

bool sortF(vector<int> &a, vector<int> &b) {
    if (a[0] == b[0])
        return a[1] < b[1];
    return a[0] < b[0];
}

int main()
{
    vector<vector <int> > v(10);
    vector<vector<int>> dirs = {{0,1},{0,-1},{1,0},{-1,0}};
    sort(dirs.begin(), dirs.end(), sortF);
    for (auto dx: dirs) {
        cout << dx[0] << ":" << dx[1] << endl;
    }
    return 0;
    //v.resize(10);
    
    for (int i =0; i < 10; i++) {
        v[i] = vector<int> (10);
        for (int j = 0; j < 10; j ++) {
            v[i][j] = i + j;
            printf("%d\n", v[i][j]);
        }
    }
    vector<int> v2 = {1};
    vector<int>::iterator it = v2.begin();
    v2.insert(it,100);
    //it  =  upper_bound(v2.begin(),v2.end(),100);
    //cout << "Lowed bound: " << *it << endl;
    //reverse(v2.begin(),v2.end());
    cout << "vector: ";
    for (auto &r : v2) {
        cout << r << "\t";
    }
    cout << endl;

    for (auto &d : dirs) {
        cout << "Dirs: " << d[0] << ": " << d[1] << endl;
    }
    
    
}
