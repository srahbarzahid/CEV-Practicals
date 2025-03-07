import java.util.Scanner;
class Complex{
   int real,imag;
   
   public void get(){
    Scanner sc = new Scanner(System.in);
    System.out.println("enter real number");
    this.real=sc.nextInt();
    System.out.println("enter imaginary number");
    this.imag=sc.nextInt();
   }
   
   public static Complex sum(Complex c1, Complex c2){
     Complex temp = new Complex();
     temp.real=c1.real+c2.real;
     temp.imag=c1.imag+c2.imag;
     return temp;
   }
  public static void main(String[] args){
    Complex c1 = new Complex();
    Complex c2 = new Complex();
    c1.get();
    c2.get();
    Complex res = sum(c1,c2);
    System.out.println("add of complex is "+res.real+"+"+res.imag+"i");
  }
 }
