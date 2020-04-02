

#include<iostream>
#include<vector>

using namespace std;


class Node
{
    public:
        Node *children[26];
        bool isWord;
        Node() {
            memset(children,0,26);
            isWord = false;
        }
};


class Trie
{
    Node *root;
    public:
    Trie() {
        root = new Node();
    }
    void addWord(string);
    bool searchWord(string);
};

void Trie::addWord(string s) {
    Node *node = root;
    cout << "Adding word: " << s;
    for (auto ch : s) {
        int index = ch - 'a';
        cout << index << endl;
        if (node->children[index] == NULL) {
            Node *child = new Node();
            node->children[index] = child;
        }
        
        node = node->children[index];
    }
    node->isWord = true;
    return;
}

bool Trie::searchWord(string s) {
    Node *node = root;
    if (node == NULL)
        return false;

    cout << endl << "searching: " << s;
    for (auto c : s) {
        int index = c - 'a';
        cout << index << endl;
        if (node->children[index] != NULL) {
            node = node->children[index];
        }
        else
            return false;
    }
    return (node->isWord == true);
}




int main() {
    vector<string> strings = {"badal"};
    Trie t = Trie();
    for (auto w: strings) {
        t.addWord(w);
    }
    if ( t.searchWord("badal") ) {
        cout <<"badal present";
    }
    if (! t.searchWord("bada")) {
        cout << "bada nott presentt";
    }
    return 0;
}
