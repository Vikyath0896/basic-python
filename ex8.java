import java.util.Scanner;

public class ex8{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int x;
        int [] flats={1,2,2,2,2,3,4};
        int count=0;
        
        
        
        System.out.println("Enter the value of x that is to be searched");
        x=sc.nextInt();
        
            for(int j=0;j<flats.length;j++){
                if(flats[j]==x){
                    count=count+1;
                }
               
            }
             
            if(count>0){
                System.out.println(count);
            }
            else{
                System.out.println("element is not presrent");
            }
         
        
        
    }
}