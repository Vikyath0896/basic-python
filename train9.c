#include<stdio.h>
#include<stdlib.h>
void difference(int n ,int m){
    int i,sum=0,sum1=0,diff=0;
    for(i=1;i<=m;i++){
    if(i%n==0){
    sum=sum+i;
    }
    else{
    sum1=sum1+i;
    }
       
    }
    
    printf("%d\n",sum);
    printf("%d\n",sum1);
    diff=sum1-sum;
    printf("%d\n",diff);

}
int main(){
    int n,m;
    printf("Enter the value of n");
    scanf("%d",&n);
    printf("Enter the value of m");
    scanf("%d",&m);
    difference(n,m);
    return 0;
}