using namespace std;
class Node {
    public:
    int key;
    int value;
    Node *next;
    Node *prev;
    Node(): next(NULL), prev(NULL),key(0),value(0) {}
    Node(int key, int value): key(key), value(value),next(NULL), prev(NULL) { }
};
class LRUQ {
    private:
    Node *front;
    Node *tail;
    public:
    LRUQ() {
        front = new Node();
        tail = new Node();
        front->next = tail;
        tail->prev = front;
    }
    void move_to_front(Node *node)  {
        if (front->next != node) {
            Node *temp = front->next;
            node->prev->next = node->next;
            node->next->prev = node->prev;
            front->next = node;
            node->prev = front;
            temp->prev = node;
            node->next = temp;
        }
    }
    
    void add_to_front(Node *node) {
        Node *temp = front->next;
        front->next = node;
        node->prev = front;
        node->next = temp;
        temp->prev = node;
    }
    
    Node *pop_from_tail() {
        Node *temp = tail->prev;
        Node *prev = temp->prev;
        
        tail->prev = prev;
        prev->next = tail;
        temp->next = temp->prev = NULL;
      
        return (temp);
    }
};
class LRUCache {
private:
    int c;
    int count;
    map <int, Node*> hash;
    LRUQ *Q;
    public:
    LRUCache(int capacity) {
        c = capacity;
        Q = new LRUQ();
        count = 0;
    }
    
    int get(int key) {
      map<int, Node*>::iterator it;
      it = hash.find(key);
      if(it == hash.end()) {
          return (-1);
      }
        Node *node = it->second;
        Q->move_to_front(node);
        return(node->value);
    }
    
    
    void put(int key, int value) {
        map<int,Node*>::iterator it;
        it = hash.find(key);
        Node *node;
        if (it == hash.end()) {
            node = new Node(key,value);
            hash[key] = node;
            Q->add_to_front(node);
            count++;
        }
        else {
            node = it->second;
            node->value = value;
            Q->move_to_front(node);
        }
        if (count > c) {
            node = Q->pop_from_tail();
            hash.erase(node->key);
            delete node;
            count--;
        }
        
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
