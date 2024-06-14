#include<stdio.h>
#include<stdlib.h>
int main(){
    int n;
    printf("Enter the month");
    scanf("%d",&n);
    if(n==12 || n==1 || n==2){
        printf("Season:Winter");
    }
    else if(n==3|| n==4 || n==5){
        printf("Season:Spring");
    }
    else if(n==6 || n==7 || n==8){
        printf("Season:Summer");
    }
    else if(n==9 || n==10 || n==11){
    printf("Season:Autumn");
    }
    else{
        printf("Invalid month");
    }



    return 0;

}