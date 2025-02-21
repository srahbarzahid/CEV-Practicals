import java.util.Scanner;

public class Arithmetic{
  public static void main(String[] args){
     int a,b;
     Scanner sc=new Scanner(System.in);
     System.out.println("enter the 2 numbers");
     a=sc.nextInt();
     b=sc.nextInt();
     
     while(true){
         System.out.println("1.Addition\n2.Substraction\n3.multipication\n4.division\n5.exit");
         System.out.println("Enter the option: ");
         int opt=sc.nextInt();
      switch(opt){
         case 1: System.out.println("Sum: "+ (a+b));
         break;
      case 2: System.out.println("Difference: "+ (a-b));
         break;
      case 3: System.out.println("Mult: "+(a*b));
      	break;
      case 4: System.out.println("Division: "+(a/b));
        break;
      case 5: return;
      default: System.out.println("invalid number");
      break;  	   
        }   
     }	
   }
 }
