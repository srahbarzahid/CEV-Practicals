import java.util.Scanner;
public class MathFun{
   public static void main(String[] args){
      Scanner sc=new Scanner(System.in);
      System.out.println("enter a word");
      String w1 = sc.nextLine();  
      System.out.println("enter another word");
      String w2 = sc.nextLine();
      System.out.println("length of the word: "+ w1.length());
      System.out.println("combining of two words:" + w1.concat(" "+w2));
      System.out.println("Uppercase of an word:" + w1.toUpperCase());
      System.out.println("lowercase an word:" + w1.toLowerCase());
      
      System.out.println("enter two numbers:");
      int a=sc.nextInt();
      int b = sc.nextInt();
      System.out.println("greatest number is:"+ (Math.max(a,b)));
      System.out.println("shortest number is:" + (Math.min(a,b)));
      System.out.println("square root of number "+a+" is: " + (Math.sqrt(a)));
      System.out.println("the random number is :" + (Math.random()*10));
    }
  }
