class Constructor{
  Constructor(){
    System.out.println("constructor is successfully runned");
  }
  void display(){
    System.out.println("just constructor sample program");
  }
  public static void main(String[] args){
    Constructor temp = new Constructor();
    temp.display();
  }
}
