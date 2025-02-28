import java.util.Scanner;
public class Car{
 
 String name;
 int year;
 
 void display(){
    System.out.println("The car "+name+" manufactured by "+year);
   }
 public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    Car c1= new Car();
    System.out.println("enter the car name and year");
    c1.name=sc.nextLine();
    c1.year=sc.nextInt(); 
    c1.display();
   }  
 }
