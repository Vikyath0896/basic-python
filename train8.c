#include<stdio.h>
int main(){
    int n,i,j;
    int k=3;
    int arr[20];
    printf("Enter teh size of array");
    scanf("%d",&n);
    printf("enter the elements of array");
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    // for(i=0;i<=n/2;i++)
    // printf("%d\t",arr[i]);
    // for(i=n/2+1;i<n;i++)
    // printf("%d\t",arr[i]);
    // printf("\n");
    // for(i=n/2;i>=0;i--)
    // printf("%d\t",arr[i]);
    // // printf("\n");
    // for(i=n-1;i>n/2;i--)
    // printf("%d\t",arr[i]);
    for(int i=0;i<n;i++)
    printf("%d\t",arr[i]);
    printf("\n");

    for(i=k-1;i>=0;i--)
    printf("%d\t",arr[i]);
    for(i=n-1;i>=k;i--)
    printf("%d\t",arr[i]);
    
     return 0;

}