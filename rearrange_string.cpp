#include <iostream>
#include <queue>
#include <map>

using namespace std;

struct CompareFreq
{
    bool operator() (const pair<char, int> n1, const pair<char, int> n2) {
        return n1.second < n2.second;
    }
};

int main()
{
    priority_queue<pair<char,int>,vector<pair<char,int> >,CompareFreq> pq;
    map<char,int> d;
    string input = "aaabc";

    for (char const &c: input) {
        d[c] += 1;
	}
    map<char,int>::iterator it;
    for(it = d.begin(); it != d.end(); it++) {
        pq.push(make_pair(it->first, it->second));
    }

    pair<char,int> prev = make_pair('#',0);
    
    string out = "";
    while (!pq.empty()) {
        pair<char,int> top = pq.top();
        out += top.first;
        pq.pop();
        if (prev.second != 0) {
            pq.push(prev);
        }
        top.second -= 1;
        prev = top;
    }
    if (input.length() == out.length()) {
        cout << out;
    } else {
        cout << "Not possible";
    }
    
}
