#include<iostream>
#include<map>
#include<vector>

using namespace std;

vector<string> util(string s, map<string,int> &m, map<string, vector<string> > &d) {
    if (d.count(s) > 0)
        return {s};

    if (s.length() == 0)
        return {};

    string res = "";
    for (const pair <string,int> &ele : m) {
        string eles = ele.first;
        if (eles.length() > s.length())
            continue;

        if (eles != s.substr(0,eles.length()))
            continue;

        if (eles.length() == s.length()) {
            res += eles;
            break;
        }
        else {
            vector<string> rest = util(s.substr(eles.length()), m, d);
            for (const string &trest : rest) {
                res = res + eles + " " + trest;
            }
        }
    }

    d[s].push_back(res);
    return {res};
    
}

void wordBreak(string s, vector<string> &wordDict) {
    map<string, int> m;
    for (const string &w : wordDict) {
        m[w] = 1;
    }
    map<string, vector<string> > d;
    vector<string> res = util(s, m, d);
    for (const string &out : res) {
        cout << out << endl;
    }
}

int main () {
    string s1 = "catsanddog";
    vector<string> w = {"cat", "cats", "and", "sand", "dog"};
    wordBreak(s1,w);
}
