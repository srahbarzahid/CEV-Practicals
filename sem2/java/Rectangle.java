import java.util.Scanner;
public class Rectangle{
  double len;
  double wid;
  double area(){
    return len*wid;
  }
  
   public static void main(String[] args){
   Scanner sc = new Scanner(System.in);
   int l,w;
     Rectangle rect1= new Rectangle();
     Rectangle rect2= new Rectangle();
     
     System.out.println("enter the length and width of rectangle1");
     l=sc.nextInt();
     w=sc.nextInt();
     rect1.len=l;
     rect1.wid=w;

	rect2.len=4;
	rect2.wid=5;
     System.out.println("Area of rectangle1:"+ rect1.area());
     System.out.println("Area of rectangle2:"+ rect2.area());
   }
  }
