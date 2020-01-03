#include <stdio.h>
#include <string.h>
#include <math.h>
#include <limits.h>

#define COUNTER_TABLE_SIZE INT_MAX
#define DATA_TABLE_SIZE 10009
#define STR_SIZE 50
#define true 1
#define false 0

int global_num_of_elements = 0;

/* Reference: https://stackoverflow.com/questions/664014/what-integer-hash-function-are-good-that-accepts-an-integer-hash-key */
unsigned int hash3_i(unsigned int x) {
    x = ((x >> 16) ^ x) * 0x45d9f3b;
    x = ((x >> 16) ^ x) * 0x45d9f3b;
    x = (x >> 16) ^ x;
    return x;
}


/* Reference: https://gist.github.com/badboy/6267743 */
unsigned int hash2(unsigned int a)
{
   a = (a+0x7ed55d16) + (a<<12);
   a = (a^0xc761c23c) ^ (a>>19);
   a = (a+0x165667b1) + (a<<5);
   a = (a+0xd3a2646c) ^ (a<<9);
   a = (a+0xfd7046c5) + (a<<3);
   a = (a^0xb55a4f09) ^ (a>>16);
   return a;
}

/* Reference : https://www.wikiwand.com/en/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function */
unsigned long
fnvhash(unsigned char *str)
{
	unsigned long hash = 0xcbf29ce484222325;
	unsigned long fnv_prime = 0x100000001b3;
	
	while(*str != '\0') {
		hash = hash * fnv_prime;
		hash = hash ^ *(str);
		str++;
	} 
	return hash;
}

unsigned long
hash_str(unsigned char *str)
{
    unsigned long hash = 5381;
    int c;

    while (c = *str++)
        hash = ((hash << 5) + hash) + c; /* hash * 33 + c */

    return hash;
}

typedef struct entry_s {
	int key;
	void *value;
	struct entry_s *next;
	struct entry_s *prev;
}entry;

typedef struct hashtable_s {
	int size;
	struct entry_s **table;	
}TABLE;


TABLE *hashtable;
TABLE *data_t;

TABLE *create( int size ) {
    printf("\nCreating table of size %d...",size);
    fflush(stdout);

	TABLE *hashtable_t = NULL;
	int i;

	if(size < 1) return NULL;

	/* Allocate the table itself. */
	if((hashtable_t = malloc(sizeof(TABLE))) == NULL) {
        perror("Malloc failed!");
		exit(1);
	}

	/* Allocate pointers to the head nodes. */
	if((hashtable_t->table = malloc(sizeof(entry *) * size)) == NULL) {
        perror("Malloc failed!");
		exit(1);
	}
	for(i = 0; i < size; i++) {
		hashtable_t->table[i] = NULL;
	}

	hashtable_t->size = size;

	return hashtable_t;	
}

int notInRange(int id)
{
    if (id >= 1 && id <= INT_MAX)
        return 1;
    else
        return 0;
}

void deleteCounterAndData(entry **Cnode)
{
    entry *temp;
    if ((*Cnode) == NULL) {
        printf("%s :: Node cannot be NULL", __FUNCTION__);
        return;
    }
    entry **dnode = &((*Cnode)->value);
    free(*Cnode);
    *Cnode = NULL;
    if ((*dnode) == NULL) {
        printf("%s :: Data Node cannot be NULL", __FUNCTION__);
        return;
    }
    if ((*dnode)->prev == NULL) {
        temp = *dnode;
        *dnode = (*dnode)->next;
    } else {
        temp = *dnode;
        (*dnode)->prev->next = (*dnode)->next;
    }
    printf("\nFreeing data: %s",(char *)temp->value);
    if (temp->value) {
        free(temp->value);
        temp->value = NULL;
    }
    free(temp);
    temp = NULL;
    global_num_of_elements--;
    return;
}

void queryCounterTable (entry **node, int qid, int delete)
{
    while ((*node) != NULL) {
       if ((*node)->key == qid) {
            if (delete) {
                return deleteCounterAndData(node);
            }
            entry *data =(entry *)(*node)->value;
            printf("Data exists: %s",data->value);
            return;
       }
        *(node) = (*node)->next;
    }
    printf("\nId is empty!");
    return;
}

void table_get(int query_id)
{
    if (!notInRange(query_id)) {
        printf("\nQuery not in range! Valid range(1-%d)",INT_MAX);
        return;
    }
    
    //int id = hash2(query_id) % COUNTER_TABLE_SIZE;
    if (hashtable->table[query_id] == NULL) {
        printf("\nId is empty!");
        return;
    } else {
        queryCounterTable(&hashtable->table[query_id], query_id, false);
    }
    return;
}

void createCounterNode(entry **node, entry *data_node)
{
   entry *new_node = NULL;
   new_node = (struct entry_s *)malloc(sizeof(entry));
   if (new_node == NULL) exit(1);
    
   memset(new_node, 0 , sizeof(*new_node));
   new_node->key = data_node->key;
   new_node->value = data_node;

   if (*(node) == NULL)
      *node = new_node;
   else {
        (*node)->next = new_node;
        new_node->prev = (*node);
   }
}

void insertInCounter(entry *dnode, int count_val)
{
    /*Earlier approach, trying to store counters in small hash table
    unsigned int idx = hash2(dnode->key) % COUNTER_TABLE_SIZE; */
    fflush(stdout);
    entry *Cnode = NULL;
    if (hashtable->table[count_val] == NULL) {
       createCounterNode(&hashtable->table[count_val], dnode);
    } else { /* This else is never executed */
        Cnode = hashtable->table[count_val];
        while(Cnode->next != NULL) 
            Cnode = Cnode->next;

        createCounterNode(&Cnode, dnode);
    }
}

int getNextGblId (void)
{   
    static int start = 1;
   
    while (hashtable->table[start] != NULL) {
        start = (start + 1) % INT_MAX;
        if (start == 0) start++;
    }
    return start;
}

void createDataNode (entry **prev, char *str)
{
    if (global_num_of_elements == INT_MAX - 1) {
        printf("\nID table is full...!");
        return;
    }
    entry *node = (struct entry_s *)malloc(sizeof(entry));
    if (node == NULL) exit(1);

    memset(node, 0, sizeof(*node));
    node->value = str;
    node->key = getNextGblId();
    
    if ((*prev) == NULL)
        *prev = node;
    else {
        (*prev)->next = node;
        node->prev = (*prev);
    }
    printf("\nData: %s key: %d", str, node->key);
    global_num_of_elements++;
    fflush(stdout);
    insertInCounter(node, node->key);
}

void insertData(char *str)
{
    int idx =  fnvhash(str) % DATA_TABLE_SIZE;
    entry *prev = NULL;
    if (data_t->table[idx] == NULL)
    {
        createDataNode(&data_t->table[idx], str);
    } else {
        entry *node = data_t->table[idx];
        while (node != NULL && 
               strncmp((char *)node->value,str,strlen(node->value)!=0)) {
            prev = node;
            node = node->next;
        }
        if (node != NULL) {
            printf("\nKey exists: %d",node->key);
            return;
        }
         createDataNode(&prev, str);
    }
}

void acceptData()
{
    char *str;
    int ch;
    size_t len = 0;
    size_t size = STR_SIZE;
    str = realloc(NULL, sizeof(char)*size);
    if(!str) exit(1);
    while(EOF!=(ch=fgetc(stdin)) && ch != '\n'){
        str[len++]=ch;
        if(len==size){
            str = realloc(str, sizeof(char)*(size+=50));
            if(!str) exit(1);
        }
    }
    str[len++]='\0';
    insertData(str);
}

void deleteDataById(int query_id)
{
    if (!notInRange(query_id)) {
        printf("\nQuery not in range! Valid range(1-%d)",INT_MAX);
        return;
    }
    
    if (hashtable->table[query_id] == NULL) {
        printf("\nId is empty!");
        return;
    } else {
        return queryCounterTable(&hashtable->table[query_id], query_id, true);
    }
}

void cleanupTables()
{
    printf("Cleaning up....");
    fflush(stdout);
    for (int i = 0; i < DATA_TABLE_SIZE; i++) {
        if (data_t->table[i])
           free(data_t->table[i]);
    }
    free(data_t);

    for (int i = 0; i < COUNTER_TABLE_SIZE; i++) {
        if (hashtable->table[i]) 
           free(hashtable->table[i]);
    }
    free(hashtable);
}

int main()
{
    hashtable = create(COUNTER_TABLE_SIZE);
    data_t = create(DATA_TABLE_SIZE);

    char ans = 'n';
    int answ = 0;
    int query_id;
    char data[1024];
    char ch;
    int id;

    while(1) {
        printf("\n1.Query\n2.Create\n3.Delete by ID\nYour option: ");
        scanf("%d",&answ);
        switch(answ) {
            case 1:
                printf("Query: Please enter ID: ");
                scanf("%d",&query_id);
                table_get(query_id);
                break;
            case 2:
                getchar();
                printf("Create: Please enter the data: ");
                acceptData();
                break;
            case 3:
                getchar();
                printf("Delete: Please enter valid ID: ");
                scanf("%d",&query_id);
                deleteDataById(query_id);
                break;
        }
        printf("\nContinue (Y/N) ?: ");
        fflush(stdout);
        scanf(" %c",&ch);
        if ((char)tolower(ch) == 'n') {
            break;
        }
    }
    cleanupTables();
}
