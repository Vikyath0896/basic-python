#include<stdio.h>
#include<stdlib.h>
int house(char ch)
{
    switch (ch)
    {
    case 'A':
        printf("Lot A has 20 items\n");
        break;
    case 'B':
        printf("Lot B has 60 items\n");
        break;
    case 'C':
        printf("Lot C has 10 items\n");
        break;
    case 'T':
        printf("Total Lots has 90 items\n");
        exit(0);
    default:printf("Invalid Lot!\n");
    }
    house(ch='T');
    return 0;
}
int main()
{
    char ch=0;
    printf("----Items----\nA\nB\nC\nEnter the Warehouse\n");
    scanf("%c",&ch);
    house(ch);
    return 0;
}