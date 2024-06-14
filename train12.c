#include<stdio.h>
#include<stdlib.h>
int sal;
float sal1,sal2,sal3;
float rat;
int main(){
printf("Enter the salary");
scanf("%d",&sal);
printf("Enter the Performance appraisal rating");
scanf("%f",&rat);
if( rat>=1 && rat<=3){
    sal1=1.1*sal;
    printf("%d",sal1);
}else if( rat>3 && rat<=4){
    sal2=1.25*sal;
    printf("%d",sal2);
}else if( rat>4 && rat<=5){
    sal3=1.30*sal;
    printf("%d",sal3);
}
if(sal==0 || sal<0 || rat>5){
    printf("Invalid input");
}

return 0;
}
