import java.util.*;
public class sort{
   String str;
   
   public void get(){
       Scanner sc = new Scanner(System.in);
       System.out.println("enter the string: ");
       this.str=sc.nextLine();
     }
   public void asc(){
       char[] arr = str.toCharArray();
       Arrays.sort(arr);
       System.out.println("sorted string is: "+new String(arr));
     }  
     public static void main(String[] args){
        sort word = new sort();
        word.get();
        word.asc();
      }
  }
