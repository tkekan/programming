
#include<iostream>

using namespace std;

typedef struct interval
{
    int low;
    int high;
}INT;

typedef struct Node
{
    interval *in;
    struct Node *left;
    struct Node *right;
    int max;
}Node;

Node * createNode(INT, Node *);
Node *newNode(INT);

Node *newNode(INT interval)
{
    Node *root = (Node *)malloc(sizeof(Node));
    root->left = NULL;
    root->right = NULL;
    root->in = new INT(interval);
    root->max = interval.high;
    return root;
}

Node *createNode(INT inter, Node *root)
{
    if ( root == NULL )
        return newNode(inter); 
    int low = inter.low;
    if ( root->in->low > low)
        root->left = createNode(inter, root->left);   
    else
        root->right = createNode(inter, root->right);

    if (root->max < inter.high )
        root->max = inter.high;
    
    return root;
}

bool doOverlap(INT *l1, INT l2)
{    
 
    if ( l1->low <= l2.high && l2.low <= l1->high ) 
        return true;
    else
        return false;
}

Node * searchOverlapping(Node *root, INT interval)
{
    if (root == NULL )
        return NULL;
   
    if (doOverlap(root->in, interval))
        return root;

    if (root->in->low > interval.low && root->left && interval.high <= root->left->max )
        root = searchOverlapping(root->left, interval);
    else 
        root = searchOverlapping(root->right, interval);  

    return root;
}

int main()
{
    INT ints[6] = { {15, 20}, {10, 30}, {17, 19},
                         {5, 20}, {12, 15}, {30, 40} }; 
    Node *root = NULL;
    int size = sizeof(ints)  / sizeof(ints[0]);
    for ( int i = 0 ; i < size; i++)
        root = createNode(ints[i], root);
    
    INT search = {10,30};
    Node *ret = NULL;
    ret = searchOverlapping(root,search);
    printf("\nResults %d %d", ret->in->low, ret->in->high);
    printf("\nRoot: %d, %d, %d",root->in->low,root->in->high,root->max);
    return 0;
    
}
