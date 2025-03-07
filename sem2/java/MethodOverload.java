class MethodOverload{

	public double add(double a,double b){
	  return (a+b);
	}
	public int add(int a,int b){
	  return (a+b);
	}
	public int add(int a,int b,int c){
	  return (a+b+c);
	}
	
     public static void main(String[] args){
      MethodOverload obj = new MethodOverload();
      
      System.out.println("sum is = "+obj.add(5.4,8.9));
      System.out.println("sum is = "+obj.add(6,7));
      System.out.println("sum is = "+obj.add(4,5,6));
     }	
  }
  
