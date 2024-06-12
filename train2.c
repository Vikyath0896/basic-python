#include<stdio.h>
void movies(int name){
    switch(name){
        case 1:printf("The ticket price is 500");
        break;
        case 2:printf("The ticket price is 1000");
        break;
        case 3:printf("The ticket price is 750");
        break;
    }
}
int main(){
     
     int n;
     printf("1.kgf 2.kgf2 3.kgf3\n");
     scanf("%d",&n);
     
     movies(n);

    return 0;
}
 