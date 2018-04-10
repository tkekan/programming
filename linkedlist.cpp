#include<iostream>

using namespace std;

struct Node
{
    Node *next;
    int data;
};

class LinkedList
{
    Node *head;
    Node *tail;
    public:
        LinkedList()
        {
            head = NULL;
            tail = NULL;   
        }
    void newNode(int data);
    void printList();
};

void LinkedList::printList()
{
    Node *tmp = head;
    while ( tmp ) {
        cout << tmp->data << "\n";
        tmp = tmp->next;
    }
}
void LinkedList::newNode(int data)
{
    Node *tmp = new Node;
    tmp->data = data;
    if ( head == NULL )
    {
        head = tmp;
        tail = tmp;
    }
    else {
        tail->next = tmp;
        tail = tail->next;
        tail->next = NULL;
    }
}


int main()
{
    LinkedList a;
    a.newNode(10);
    a.newNode(20);
    a.printList();
}
