#include<stdio.h>
#include<string.h>
int main()
{
char str[] = "dir1/dir2/./../dir3/dir4/../dir5";
const char *del = "/";
char *res = NULL;
res = strtok(str,del);
while ( res != NULL )
{
res = strtok(NULL,del);
printf("%s\n",res);
}
return 0;
}
