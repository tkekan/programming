

#include<iostream>
#include<vector>
using namespace std;

int main()
{
    string tp = "123";
    cout << stoi(tp);
    int i = 1;
    tp += to_string(i);
    cout << "string is :" << tp << endl;
    string one = "11";
    string two = "1";
    vector<int> res;
    int carry = 0;     
    int minlen = min(one.length(), two.length());
    int total = 0;
    for (int i = minlen-1; i >= 0 ; i--) {
        total = (int)(one[i] - '0') + (int)(two[i] - '0') + carry;
        carry = total / 2;
        total = total % 2;
        res.push_back(total);
    }

    if (one.length() != minlen) {
        
    }
    if (carry > 0) {
        res.push_back(carry);
    }

    reverse(res.begin(),res.end());
    for (int &i : res) {
        cout << i;
    } 
        

}
