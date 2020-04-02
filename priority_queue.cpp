

#include<iostream>
#include<queue>

using namespace std;

class Node {
    int data;
    public:
        Node(int d):data(d) {}
        int getdata() const{ return data; }
};

class Compare {
    public:
    bool operator() (const Node *lhs, const Node *rhs) 
    {
        return lhs->getdata() > rhs->getdata();
    }
};


int main()
{
    vector<Node *> v1 = { new Node(10), new Node(-1), new Node(0), new Node(20), new Node(5) };
    priority_queue<Node *, vector<Node *>, Compare> pq;

    for (auto n: v1) {
        pq.push(n);
    }

    while (pq.size() > 0) {
        auto n = pq.top();
        cout << n->getdata() << endl;
        pq.pop();
    }

    return 0;
}
