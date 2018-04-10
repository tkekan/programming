#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int vercmp( char *v1, char* v2) {
int it1 = 0;
int it2 = 0;
int index1 = 0;
int index2 = 0;
int first, second;

char *string1 = (char *)malloc(strlen(v1)+1);
memset(string1,'\0',strlen(v1)+1);
char *string2 =(char *)malloc(strlen(v2)+1);
memset(string2,'\0',strlen(v2)+1);


 while(v1[it1] != '\0' || v2[it2] != '\0') {
   while(v1[it1] != '.')
    {
     if( v1[it1] == '\0')
         break;
       // index = it1;
       it1++;
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

}


int main()
{

   char *v1 = "1.2.3";
   char *v2 = "1.2.3.1";

   int value = vercmp(v1,v2);

   printf("%d",value);
}
