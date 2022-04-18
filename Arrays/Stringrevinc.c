#include <stdio.h>
#include <string.h>

void trimleading(char *s)
{
	int i,j;
	for(i=0;s[i]==' '||s[i]=='\t';i++);
 
	for(j=0;s[i];i++)
	{
		s[j++]=s[i];
	}
	s[j]='\0';  
}
int main()
{
   char s[100];
   gets(s);
    trimleading(s);
   strrev(s);
    trimleading(s);
   printf("%s", s);

   return 0;
}