#include<iostream>
#include<vector>

using namespace std;

int main() {
    std::string s = "scott,tiger,mushroom";
    std::string delimiter = ",";
    vector<string> res;

    size_t pos = 0;
    std::string token;

    while ((pos = s.find(delimiter)) != std::string::npos) {
        token = s.substr(0,pos);
        res.push_back(token);
        s.erase(0, pos + delimiter.length());
    }
    res.push_back(s);
    for (auto &temp : res) {
        temp[0] = 'T';
    }
    for (auto &temp : res) 
        cout << temp;
}
