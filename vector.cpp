#include<iostream>
#include<vector>
#include <algorithm> 
#include <queue>
#include <iomanip>

using namespace std;

bool sortF(vector<int> &a, vector<int> &b) {
    if (a[0] == b[0])
        return a[1] < b[1];
    return a[0] < b[0];
}


void queue_ds() {
    queue<pair<string,int>> q;
    
    string s = "cog";
    cout << s.substr(0,-1) + "_" + s.substr(2);
    for (int i=0; i < s.length(); i+=1) {
        if (i == 0) {
            cout << "_" + s.substr(i+1) << endl;
        }
        string newstr = s.substr(0,i) + "_" + s.substr(i+1);
        cout << newstr << endl;
    }
    q.push(make_pair("cog",1));
    while (q.size() > 0) {
        auto p = q.front();
        q.pop();
        cout << p.first << p.second;
    }
    
}
int main()
{

    //queue_ds();
    int i = '1' - '0';
    cout << "Int value" << i;
    vector<vector <int> > v(10);
    vector<vector<int>> dirs = {{0,1},{0,-1},{1,0},{-1,0}};
    sort(dirs.begin(), dirs.end(), sortF);
    string s = "abc";
    for (int i = 0; i < s.size(); i+= 1) {
        if (s[i] != s[i+100])
            cout << "Not equal" << s[i] << s[i+1] << endl;
    }
        
    for (auto dx: dirs) {
        cout << dx[0] << ":" << dx[1] << endl;
    }

    vector<vector<int>> v3 (3);
    cout << "Tanvir: " << v3.size() << endl; 

    vector<int> v4 (10,-1);
    cout << "V4: " << v4.size() << endl;
    for (int i = 0; i < v4.size(); i++) {
        cout << v4[i] << setw(4);
    }
    vector<int> copy = {1,2,3};
    sort(copy.begin(), copy.end(), greater<int>());
    for (int i = 0 ; i < v3.size(); i+=1) {
        v3[i].resize(3);
        v3[i] = copy;
    }
    cout << "Tanvir: " << v3.size() << v3[0].size();
    return 0;

    for (auto i : v3[0]) 
        cout << i << "\t";

    
    

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
