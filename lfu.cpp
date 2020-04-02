#include<iostream>
#include<unordered_map>
#include <list>

using namespace std;

struct Node{
    int key;
    int value;
    int fre;
    Node(int x,int y,int z):key(x),value(y),fre(z){}
};

int main()
{

    int key = 1;
    int value = key;
    unordered_map<int,list<Node>> frelist;
    list<Node>& newlist=frelist[1];
    newlist.push_front(Node(key,value,1));
    for (auto it: newlist) {
        cout << it.key << it.value << it.fre << endl;
    }
}
