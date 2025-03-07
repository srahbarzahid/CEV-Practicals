class RectConstrctr{
   double len;
   double wid;
   
   RectConstrctr(){
     this.len=10;
     this.wid=3;
   }
   RectConstrctr(double len){
      this.len=len;
      this.wid=8;
    }
    
   RectConstrctr(double len,double wid){
       this.len=len;
       this.wid=wid;
     }
   double area(){
       return len*wid;
     }  
    public static void main(String[] args){
       RectConstrctr rect1= new RectConstrctr();
       RectConstrctr rect2 = new RectConstrctr(3);
       RectConstrctr rect3 = new RectConstrctr(4,5);
       
       System.out.println("area of rectangle1 is: "+rect1.area());
       System.out.println("area of rectangle2 is: "+rect2.area());
       System.out.println("area of rectangle3 is: "+rect3.area());
     }  
  }
