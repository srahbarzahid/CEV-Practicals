import java.util.Scanner;
public class array{
   public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    System.out.println("enter the size of array: ");
    int n = sc.nextInt();
    int[] arr=new int[n];
    System.out.println("enter the array:");
    for(int i=0;i<n;++i){
     arr[i]=sc.nextInt();
    }
    System.out.println("the values are:");
    for(int i=0;i<n;++i){
     System.out.println(" "+ arr[i]);
    }
    int sum =0;
    for(int i=0;i<n;++i){
       sum+=arr[i];    
    }
    System.out.println("sum of values:" + sum);
   }
 }
