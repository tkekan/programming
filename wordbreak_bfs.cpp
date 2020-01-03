#include<iostream>
#include<queue>
#include<unordered_set>

using namespace std;

bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> myset;
        queue<int> myq;
        if (s.length() == 0)
            return false;
        myq.push(0);
        for (const string &s: wordDict){
            myset.insert(s);
        }
        while (!myq.empty()) {
            int start = myq.front();
            myq.pop();
            for (int end = start; end < s.length(); end++){
                if (myset.count(s.substr(start,end-start+1)) > 0) {
                    myq.push(end+1);
                    if (end+1 == s.length())
                        return true;
                }
            }
        }
      return false;
}

int main()
{
    vector<string> words = {"l","leet","code","e"};
    string s = "leetcode";
    cout << wordBreak(s,words);
}
