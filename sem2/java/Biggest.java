import java.util.Scanner;
public class Biggest{
    public static void main(String[] args){
       Scanner sc = new Scanner(System.in);
       System.out.println("enter the 3 numbers");
       int a=sc.nextInt();
       int b=sc.nextInt();
       int c=sc.nextInt();
       
       if(a>b && a>c){
          System.out.println("greatest number:"+a);
        }
       else if(b>a && b>c){
         System.out.println("greatest number:"+b);
       }else{
         System.out.println("greatest number: "+c);
       } 
       sc.close();
     }
  }
