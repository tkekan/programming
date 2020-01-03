
#include<iostream>
#include<map>
using namespace std;

map<string,int> mymap;

void countFrequency(string &word)
{
    if (!word.empty())  {
        mymap[word] += 1;
        cout << mymap[word];
        //cout << word << endl;
    }
    word.erase();
}


int main() {
    string paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.";
    string word = "";
    for (const auto& c: paragraph) {
            if (isalpha(c)) { 
                word += tolower(c); 
            } else { 
                countFrequency(word); 
            }
    }
}
