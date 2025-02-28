public class Test{
  int sum(int a, int b){
    return (a+b);
  }
  int sum(int a,int b,int c){
    return (a+b+c);
  }
  double sum(double a,double b,double c){
   return (a+b+c);
  }
  
  public static void main(String[] args){
    Test t1= new Test();
    System.out.println("sum: "+t1.sum(4,5));
    System.out.println("sum: "+t1.sum(4,6,7));
    System.out.println("sum: "+t1.sum(2.4,10.5,7.8));
  }
 }
