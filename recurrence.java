import java.util.*;
public class recurrence {
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        int flat []={0,3,1,1,2,2,5,8,7,7};
        int n=5;
        int count=0;
        for(int i=0;i<flat.length;i++){
            for(int j=i+1;j<flat.length;j++){
                if(flat[i]==flat[j]){
                    System.out.println(flat[j]);
                }
                }
            }
        }
        
    }

