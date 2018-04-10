
#include<iostream>
#include<string>
#include <unordered_map>
using namespace std;
unordered_map<string,bool> mymap;

void checkpalindrome(string str, int left, int right)
{
    int length = 1;
    string sub;
    while ( left >=0 && right < str.length() && str[left] == str[right]) {
        sub = str.substr(left, right - left + 1);
        unordered_map<string,bool>::const_iterator got = mymap.find(sub);
        if (got == mymap.end() )
            mymap[sub] = true;
        length+=1;
        left--;
        right++;
    }

}
int main()
{
    string str = "aaaaa";
    cout << "first" << str.substr(0,1) << endl;
    for ( int i = 0 ; i < str.length(); i++ ) {
        checkpalindrome(str, i, i);
        checkpalindrome( str, i, i+1);
    }
    for ( const auto&x : mymap )
        cout<<x.first <<endl;
    return 0;
    
}
