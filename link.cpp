#include <iostream>

using namespace std;

typedef struct Node Node;

struct Node
{
  Node *next;
  int data;
};


Node * getree(int data)
{
  Node *temp =(Node *)malloc(sizeof(Node));
  temp->data = data;
  temp->next = NULL;
}


void display(Node *root)
{
  while(root != NULL)
  {
     cout << root->data << "\t";
     root = root->next;
  }

}

Node * reverse(Node *root, Node **newHead)
{
    if(root->next == NULL) {
        *newHead = root;
        return root;
    }
    else {
        Node *Newstart = reverse(root->next, newHead);
        Newstart->next = root;
        Newstart = Newstart->next;
    Newstart->next = NULL;
    return Newstart;
    }


}

struct tree
{
  struct tree* left;
  struct tree* right;
  int data;
};


struct tree* newNode(int data)
{
   struct tree *temp=(struct tree *)malloc(sizeof(struct tree));
   temp->data = data;
   temp->left = NULL;
   temp->right = NULL;
   return temp;
}

#if 0
struct tree* linkedListToBSTUtil(struct Node **head, int start,int end)
{
            if (start > end)
                   return NULL;
             
            int mid = start+(end-start)/2;
            struct tree *leftChild = linkedListToBSTUtil(head,start,mid-1);
            struct tree *root = newNode((*head)->data);
            root->left = leftChild;
            *head = (*head)->next;
            root->right = linkedListToBSTUtil(head, mid+1,end);
            return root;
}



 
/* The main function that constructs balanced BST and returns root of it.
          head_ref -->  Pointer to pointer to head node of linked list
                 n  --> No. of nodes in Linked List */
struct tree* sortedListToBSTRecur(Node **head_ref, int n)
{
        /* Base Case */
        if (n <= 0)
                    return NULL;
         
            /* Recursively construct the left subtree */
            struct tree *left = sortedListToBSTRecur(head_ref, n/2);
             
                /* Allocate memory for root, and link the above constructed left 
                          subtree with root */
                struct tree *root = newNode((*head_ref)->data);
                    root->left = left;
                     
                        /* Change head pointer of Linked List for parent recursive calls */
                        *head_ref = (*head_ref)->next;
                         
                            /* Recursively construct the right subtree and link it with root 
                                     The number of nodes in right subtree  is total nodes - nodes in 
                                           left subtree - 1 (for root) which is n-n/2-1*/
                            root->right = sortedListToBSTRecur(head_ref, n-n/2-1);
                             
                                return root;
}

struct tree* sortedListToBST(Node *head)
{
        /*Count the number of nodes in Linked List */
         
            /* Construct BST */
            return sortedListToBSTRecur(&head, 5);
}
#endif

struct tree* sortedListToBST(Node **list, int start, int end) {
  if (start > end) return NULL;
  // same as (start+end)/2, avoids overflow
  int mid = start + (end - start) / 2;
  tree *leftChild = sortedListToBST(list, start, mid-1);
  tree *parent = newNode((*list)->data);
  parent->left = leftChild;
  *list = (*list)->next;
  parent->right = sortedListToBST(list, mid+1, end);
  return parent;
}
 
struct tree* sortedListToBST(Node *head, int n) {
  return sortedListToBST(&head, 0, 4);
}

int main()
{

    Node *root = getree(1);
    root->next = getree(2);
    root->next->next = getree(3);
    root->next->next->next = getree(4);
    root->next->next->next->next = getree(5);
    cout << endl;
    display(root);
    cout << endl;
   // Node *newHead = NULL;
   // Node *temp = reverse(root, &newHead);
  //  display(newHead);

// struct tree *troot = linkedListToBSTUtil(&root, 0, 4);
struct tree* troot =  sortedListToBST(root,4);
cout <<"Hello";
}
