
#include<stdio.h>
#include<stdlib.h>


typedef struct Node
{
    int data;
    struct Node *left;
    struct Node *right;
}NODE;

NODE * createBST(NODE *root)
{
    root = (NODE *)malloc(sizeof(NODE));
    if (root == NULL) {
        printf("\n%d mallloc failed");
        return NULL;
    }
    root->data = 1;
    root->left = (NODE *)malloc(sizeof(NODE));
    root->left->data = 2;
    root->right = (NODE *)malloc(sizeof(NODE));
    root->right->data = 3;
    return root;
}

int validateBST(NODE *root, NODE **prev)
{
    if (root == NULL)
        return 1;
    if ( !validateBST(root->left, prev))
        return 0;
    if ( *prev == NULL) {
        *prev = root;
        return 1;
    }
    else {
        if ((*prev)->data < root->data)
            return 1;
        else
            return 0;
    }

}

int main()
{
    NODE *root = NULL;

    root = createBST(root);
    NODE *prev = NULL;
    if ( !validateBST(root, &prev))
        printf ( "\nInValid BST");
    else
        printf("\nValid");
}
