#include <iostream>

#include <unordered_map>
#include <string>
#include <vector>
using namespace std;
//using namespace tr1;

int main()
{
    unordered_map<char,char> mapi;
    string from = "lod";
    string to = "xpf";
    string input = "Hello World";
    string output = "";
    vector<string> v1 = { "xyzzy", "plugh", "abracadabra" };
vector<string> v2({ "xyzzy", "plugh", "abracadabra" });
vector<string> v3{ "xyzzy", "plugh", "abracadabra" }; 
    int i;

    for(int i=0 ;i<from.length(); i++) {
        mapi[from[i]] = to[i];
    }

    unordered_map<char,char>::const_iterator got;
    for (int i = 0 ; i < input.length(); i++)
    {
        got = mapi.find(input[i]);
        if(got == mapi.end()) {
            output+= input[i];
        }
        else 
            output+= got->second;
    
    }
        cout << output;
}
