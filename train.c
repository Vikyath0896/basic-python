#include<stdio.h>
#include<string.h>
int main(){
   //  char str1[20]="Helloworld";
   //  char str2[20];
   //  int i,j;
   // int n= strlen(str1);
   // // printf("%d",n);
   // for( i=n-1;i!=0;i--){
   //    for(j=0;;j++){
   //       str2[j]=str1[i];
   //    }
   // }
   // str2[j]='\0';
   // printf("Reversed string is %s",str2[i]);
   char str1[20] = "Helloworld";
    char str2[20];
    int i, j;
    int n = strlen(str1);

    // Reverse the string
    for (i = n - 1, j = 0; i >= 0; i--, j++) {
        str2[j] = str1[i];
    }
    str2[j] = '\0'; // Null-terminate the reversed string

    printf("Reversed string is %s\n", str2);
   return 0;
}
