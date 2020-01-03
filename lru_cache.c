#include<stdio.h>
#include<stdlib.h>


typedef struct node_
{
    char data[100];
    struct node_ *next;
    struct node_ *prev;

}NODE;

typedef struct double_linked
{
    NODE *front;
    NODE *rear;

}DL;

typedef struct entry_
{
    void *data;
}entry_s;

typedef struct hashtable
{
    entry_s **table;
    int size
}ht;

ht *htable;
DL dll;


void insert_to_head_dll(NODE *tmp)
{
    if (dll.front == NULL && dll.rear == NULL) {
        dll.front = dll.rear = tmp;
    }
    else {
        dll.rear->next = tmp;
        tmp->prev = dll.rear;
        dll.rear = tmp;
    }

}

void insert_into_lru(int key, char *data)
{   
    int index =  key % htable->size;
    if (htable->table[index] == NULL) {
        NODE *tmp =(NODE *)malloc(sizeof(NODE));
        strcpy(tmp->data, data);
        htable->table[index] = (void *)tmp;
        printf("Inserted %s at index %d\n", data, index);
        insert_to_head_dll(tmp);
    }

}

void create_hash_table(int size)
{
    htable =(ht *)malloc(sizeof(ht));
    htable->table =(entry_s **)malloc(sizeof(entry_s *) * size);
    for (int i = 0; i < size; i++)
    {
        htable->table[i] = NULL;
    }
    htable->size = size;
}

void init_doubly_linked_list()
{
    dll.front = NULL;
    dll.rear = NULL;

}
void check_for_data(int key)
{
    printf("Checking data for key %d\n", key);
    int index = key % htable->size;
    if (htable->table[index] == NULL) {
        printf("No data at index: %d\n", index);
    }
    else {
        NODE *node = (NODE *)htable->table[index];
        printf("Found data: %s for key %d\n", node->data, key);
    }
}

int main()
{
  create_hash_table(20);
  printf("Created hash_table\n");
  init_doubly_linked_list();
  insert_into_lru(1,"tanvir");
  check_for_data(1);
    
}
