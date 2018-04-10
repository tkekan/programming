#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int vercmp( char *v1, char* v2) {
int it1 = 0;
int it2 = 0;
int index1 = 0;
int index2 = 0;
int first = 0;
int second = 0;

char *string1 = (char *)malloc(strlen(v1)+1);
memset(string1,'\0',strlen(v1)+1);
char *string2 =(char *)malloc(strlen(v2)+1);
memset(string2,'\0',strlen(v2)+1);

int len1 = strlen(v1);
int len2 = strlen(v2);

int power = 1;
int strit = 0;
while(len1 >= 0) {
 if(v1[index1] =='.' || v1[index1] == '\0')
 {
     first = (first * power) + atoi(string1);
     if(v1[index1] == '\0')
             break;
     power = power * 10;
     index1++;
     len1--;
     memset(string1,'\0',strlen(string1));
     strit = 0;
     
 }
   string1[strit++] = v1[index1++];
   len1--;
}

  printf("\n%d", first);


#if 0

 while(len1 > 0 || len2 > 0 ) {
   while(v1[it1] != '.')
    {
     if( v1[it1] == '\0')
         break;
       // index = it1;
       it1++;
       len1--;
    } 
      if(it1 > index1)
       {   
         strncpy(string1 , v1+index1,it1-index1);
         first = atoi(string1);
       }
         else first = -1;
        
   while(v2[it2] != '.' )
   {
     if( v2[it2] == '\0')
         break;
     it2++;
   }
   if( it2 > index2) {
      strncpy(string2, v2+index2, it2-index2);
      second = atoi(string2);
   }
      else second = -1;

    if(first > second)
        return 1;
    else if(second > first )
        return -1;

    it1++;
    it2++;
    index1 = it1;
    index2 = it2;

    memset(string1,'\0',strlen(string1)+1);
    memset(string1,'\0',strlen(string2)+1);

 }

  free(string1);
  free(string2);

  return 0;

#endif
  free(string1);
  free(String2);

}


char * remove(char *v1, char *v2)
{
    if( v1 == NULL || v2 == NULL )
        return NULL;
    char *output =(char *)malloc(strlen(v1)+1);

}

int main()
{

   char *v1 = "crazy for code";
   char *v2 = "code";

   //int value = vercmp(v1,v2);

   char *output = remove(v1,v2);

   printf("%d",value);
}
