#include<stdio.h>
int areaoftriangle(int b,int h){
    int area;
    area= 0.5*b*h;
    return area;
}
float areaofcircle(float r){
    float area1;
    area1=3.14*r*r;
    return area1;
}
int areaofsquare(int s){
    int area2;
    area2=s*s;
    return area2;
}
int main(){
    
    int breadth=10;
    int height=10;
    float radius=10;
    int side=10;
    int area2=areaofsquare(side);
    float area1=areaofcircle(radius);
    int area=areaoftriangle(breadth,height);
    printf("The area of a triangle is %d\n",area);
    printf("the area of circle is %f\n",area1);
    printf("the area of a square is %d",area2);

return 0;
}