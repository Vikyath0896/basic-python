#include<stdio.h>
#include<stdlib.h>
struct node{
    int info;
    struct node* link;
}*start1=NULL,*temp,*ptr;
void insertbeg(){
    temp = (struct node *)malloc(sizeof(struct node));
    printf("Enter the data\n");
    scanf("%d",&temp->info);
    temp->link = NULL;

    if(start1 == NULL)
    start1 = temp;

    else {
        temp->link = start1;
        start1 = temp;
    }//end of else

}//end of insertbeg
int main(){
int i,n;
printf("Enter the number of nodes");
scanf("%d",&n);
for(i=0;i<n;i++)
insertbeg();
return 0;
}

