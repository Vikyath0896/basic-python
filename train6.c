#include<stdio.h>
#include<string.h>

struct movie{
    char name[50];
    int price;
};
char movies[50][50] = {"hitman", "nemo", "oppenhiemer"};
int showPrice(char *name){
    for(int i = 0; i < 3; i++){
        if(strcmp(name, movies[i])){
            return i;
        }
    }
}

int main(){
    struct movie movies[10];

    while(1){
        printf("------MOVIES------\n");
        // for(int i = 0; i < 3; i++){
        //     printf("%s. %s \n",i,movies[i]);
        // }
        char name[50];
        printf("Enter the movie name: ");
        scanf("%s",name);
        switch (showPrice(name)){
            case 0:
                printf("Rs. 120\n");
                break;
            case 1:
                printf("Rs. 150\n");
                break;
            case 2:
                printf("Rs. 300\n");
                break;
            default:
                printf("Invalid movie name\n");
        }
    }
    return 0;
}