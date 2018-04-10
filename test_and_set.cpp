#include<iostream>
#include<pthread.h>
#include<cstdlib>
#include<unistd.h>
volatile int lock = 0;
#define LOCKED 1

int test_and_set(volatile int *lock)
{
    int old_val;
    old_val = *lock;
    *lock = LOCKED;
    return old_val;
}

void *critical_section(void *val)
{
    while(test_and_set(&lock) == 1) {
        printf("waiting - %jd\n",(int *)val);
        sleep(1);
    }
    
    printf("I have entered -  %d\n",(int *)val);
    sleep(10);
    lock = 0;
    pthread_exit(NULL);
}

int main()
{
    pthread_t t1,t2;
    printf("Creating thread 1\n");
    int rc =  pthread_create(&t1, NULL, &critical_section, (void *)10);
    if (rc) 
        printf("Error!! - 10");

    printf("Creating thread 2\n");
    rc =  pthread_create(&t2, NULL, critical_section, (void *)20);
    if (rc) 
        printf("Error!! - 20\n");

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    return 0;

}
