#include <linux/version.h>
#include<stdio.h>

int main()
{
printf("\n%d",LINUX_VERSION_CODE);
printf("\n%d",KERNEL_VERSION(4,4,0));
return 0;
}
