
#include <iostream>
#include <vector>

//using namespace std;

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

int findMinimum(Node *root)
{
	if( root == NULL ) 
	    return INT_MAX;

 	int left = findMinimum(root->left);
        int right = findMinimum( root->right);

        return (left < right ? ((left < root->data) ? left : root->data) : ( right < root->data ? right : root->data ));

}

void findPaths(Node *root, int cSum, int eSum, vector<int> paths)
{
    cSum += root->data;
    paths.push_back(root->data);

    int iLeaf = (root->left == NULL && root -> right == NULL);
    if( cSum == eSum && iLeaf )
    {
        for( vector <int>:: iterator it = paths.begin(); it!= paths.end() ; ++it)
        {
            cout << *it << "\t";
        
        }
    
    }

}


int main()
{
    int minData = 0;

    Node *root        = newNode(10);
    root->left        = newNode(12);
    root->right       = newNode(15);
    root->left->left  = newNode(25);
    root->left->right = newNode(30);
    root->right->left = newNode(36);
   minData = findMinimum(root);
   printf("Minimum is %d",minData);
    return 0;
}
