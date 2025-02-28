public class Animal{
   String name;
   String property;
   
   void display(){
     System.out.println("The animal name "+name+" with properties "+property);
   } 
   public static void main(String[] args){
     Animal dog=new Animal();
   dog.name="Dog";
   dog.property="dog has 4 legs";
   dog.display();
   Animal cat = new Animal();
   cat.name="cat";
   cat.property ="we can use like an pet";
   cat.display();
   }
  }
