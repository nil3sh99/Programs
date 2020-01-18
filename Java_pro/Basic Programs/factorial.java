import java.util.Scanner;

class factorial{
    public static void main(String args[]){
        System.out.print("Enter the number: ");
        Scanner input = new Scanner(System.in);
        int a = input.nextInt();
        int i,res=1;
        for(i = a; i>0; i--){
            res = res*i;
        }
        System.out.print(res);
    };
}
