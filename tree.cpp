
#include <iostream>
#include <vector>
#include <stack>

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

int findMinimum(Node *root)
{
	if( root == NULL ) 
	    return INT_MAX;

 	int left = findMinimum(root->left);
        int right = findMinimum( root->right);

        return (left < right ? ((left < root->data) ? left : root->data) : ( right < root->data ? right : root->data ));

}

void findPaths(Node *root, int cSum, int eSum, vector <int > paths)
{
    cSum += root->data;
    paths.push_back(root->data);

    int iLeaf = (root->left == NULL && root -> right == NULL);
    if( cSum == eSum && iLeaf )
    {
        for( vector <int>:: iterator it = paths.begin(); it!= paths.end() ; ++it)
        {
            cout <<*it << "\t";
        
        }
    
    }

    if( root->left !=NULL )
        findPaths(root->left, cSum, eSum, paths);
    if( root->right !=NULL )
        findPaths(root->right, cSum, eSum, paths);


    paths.pop_back();
}

bool printpaths( Node *root, vector <int> &p)
{
  if(root != NULL)
      p.push_back(root->data);
  else 
      return true;
  
  bool left =  printpaths(root->left, p);
  bool right = printpaths(root->right, p);
  
  if(left && right)
  {
      vector <int> ::iterator it;
      cout << endl;
      for ( it = p.begin(); it!=p.end() ; it++)
      {

         cout <<*it;
      }
      p.pop_back();
      return false;
  }
  else {
      p.pop_back();
      return false;
  
  }
  

}
 
/* Print nodes at a given level */
void printGivenLevel(struct Node* root, int level)
{
      if(root == NULL)
              return;
        if(level == 1)
                printf("%d ", root->data);
          else if (level > 1)
                {
                   printGivenLevel(root->left, level-1);
                   printGivenLevel(root->right, level-1);
                }
}



void printLevelOrder(struct Node* root)
{
      int h = 3;//height(root);
        int i;
        cout <<endl<<endl;
          for(i=1; i<=h; i++)
                  printGivenLevel(root, i);
}     


Node* constructTree ( int pre[], int size )
{
        // Create a stack of capacity equal to size
         
            // The first element of pre[] is always root
       stack <Node *> mystack;
       Node* root = newNode( pre[0] );
             
                // Push root
       mystack.push(root);
                 
       int i;
       Node* temp;
                         
                            // Iterate through rest of the size-1 items of given preorder array
       for ( i = 1; i < size; ++i )
          {
            temp = NULL;
                                                
            /* Keep on popping while the next value is greater than
             stack's top value. */
            while ( !mystack.empty() && pre[i] > mystack.top()->data ) {
                temp = mystack.top();
                mystack.pop();
            }
                                                         
           // Make this greater value as the right child and push it to the stack
           if ( temp != NULL)
           {
            temp->right = newNode( pre[i] );
            mystack.push(temp->right);
           // push( stack, temp->right );
           }
                                                                 
                                                                        // If the next value is less than the stack's top value, make this value
                                                                        // as the left child of the stack's top node. Push the new node to stack
           else
           {
             mystack.top()->left = newNode( pre[i] );
             mystack.push(mystack.top()->left);
           //  push( stack, peek( stack )->left );
           }
        }
             return root;
}

int printht(Node *root)
{
    if (root == NULL)
        return 0;

    int dl = printht(root->left);
    int dr = printht(root->right);

    if( dl > dr)
        return (1 + dl);
    else return (1 + dr);

}
int main()
{
    int minData = 0;
    vector <int> pa;
    Node *root        = newNode(10);
    root->left        = newNode(12);
    root->right       = newNode(15);
    root->left->left  = newNode(25);
    root->left->right = newNode(30);
    root->right->left = newNode(36);
   //minData = findMinimum(root);
   //printf("Minimum is %d",minData);
   bool value = printpaths(root, pa);
   int pre [] = {10, 5 , 1, 7, 40, 50};
   int size = sizeof(pre)/sizeof(pre[0]);
   Node *newRoot = constructTree( pre, size);
   printLevelOrder(root);
   cout << endl << "Height of tree: ";
   cout << printht(root);
    return 0;
}
