#include<stdio.h>

int main(){
    char stor;
    printf("Enter storage units A,B,C,D");
    scanf("%c",&stor);
    switch(stor){
        case 'A':storage();
        break;
    }
    return 0;
}