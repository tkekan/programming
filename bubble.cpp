
#include<iostream>
#define n 4
using namespace std;

typedef struct heapNode
{
    int element;
    int index;
    int next;
}heapNode;

void swap(heapNode *x, heapNode *y);
class Heap
{
    heapNode *harr;
    int size;
    public:
        void minHeapify(int);
        Heap(heapNode arr[], int size);    
        int getLeft(int i) { return (2*i + 1); }
        int getRight(int i) { return (2 * i + 2); }
        heapNode getMin() { return harr[0]; }
        void replaceMin(heapNode x) { harr[0] = x; minHeapify(0); }
};

Heap::Heap(heapNode node[], int size)
{
    size = size;
    harr = node;
    int pindex = (size - 1) / 2;
    while ( pindex >= 0 )
    {
        minHeapify(pindex);
        pindex--;
    }
}

void Heap::minHeapify(int i)
{
   int l = getLeft(i);
   int r = getRight(i);
   int smallest = i;

   if ( l < size && harr[l].element < harr[smallest].element)
        smallest = l;
   if ( r < size && harr[r].element < harr[smallest].element)
        smallest = r;

    if ( smallest != i )
    {
        swap(&harr[i], &harr[smallest]);
    }  
}

void swap(heapNode *x, heapNode *y)
{
    heapNode temp = *x;
    *x = *y;
    *y = temp;
}


int * mergearrays(int arr[][n], int k)
{
    int *output = new int[n*k];
    heapNode *harr = new heapNode[k];
    for ( int i = 0 ; i < k; i++){
        harr[i].element = arr[i][0];
        harr[i].index = i;
        harr[i].next = 1;
    }
    
    Heap hp(harr, k);
    for(int count = 0 ; count <= n*k; count++)    
    {
        heapNode root = hp.getMin();
        output[count] = root.element;
        
        if (root.next < n)
        {
            root.element = arr[root.index][root.next];
            root.next += 1;
        }
        else
            root.element = INT_MAX;

        hp.replaceMin(root);
    }


    return output;
}

void printarrays(int *output, int size)
{
    for (int i=0; i < size; i++)
        printf("%d ",output[i]);
}
int main()
{
    int arr[][n] =  {{2, 6, 12, 34},
                     {1, 9, 20, 1000},
                     {23, 34, 90, 2000}};

    int *output = mergearrays(arr, 3);
    printarrays(output, n*3);
    return 0;
}
