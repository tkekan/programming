
#include <iostream>
//#include <stdlib.h>
//#include <limits.h>
using namespace std;


typedef struct Node Node;


struct Node 
{
  Node *left;
  Node *right;
  int data;
};

//initializetree(Node *root)


Node * newNode(int data)
{
  Node* new_node =(Node *)malloc(sizeof(Node));
  new_node->data = data;
  return new_node;
}


bool isBst(Node *root)
{
   
   if(root == NULL)
	return true;

   bool left = isBst(root->left);
   bool right = isBst(root->right);
   if( left && right ) {
    if(root->left && root->right)
        return (root->left->data < root->data && root->right->data > root->data);
    else if( root->left )
        return ( root->left->data < root->data);
    else if ( root->right )
        return (root->right->data > root->data );
   }

   return(left && right );

}

int findMinimum(Node *root)
{
	if( root == NULL ) 
	    return INT_MAX;

 	int left = findMinimum(root->left);
        int right = findMinimum( root->right);

        return (left < right ? ((left < root->data) ? left : root->data) : ( right < root->data ? right : root->data ));

}

int main()
{
    int minData = 0;
    bool istree = true;
    Node *root        = newNode(10);
    root->left        = newNode(6);
    root->right       = newNode(14);
    root->left->left  = newNode(4);
    root->left->right = newNode(8);
    root->right->left = newNode(12);
    root->right->right = newNode(16);
    root->right->right->right = newNode(15);
   //minData = findMinimum(root);
   //printf("Minimum is %d",minData);
   if(isBst(root))
       cout<<"A bst";
   else
       cout <<"Not";
    return 0;
}
