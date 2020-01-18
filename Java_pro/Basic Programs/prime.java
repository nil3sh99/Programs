import java.util.Scanner;

class prime{
    public static void main(String args[]){
    // WAP to check the prime number
    Scanner input = new Scanner(System.in);
    System.out.print("Enter the number: ");
    int a =  input.nextInt();
    //System.out.print(a2);
    int i;
    boolean flag = false;
    if(a ==0 || a == 1){
        System.out.print("not a prime number");
    }
    for(i=2; i<= a/2; i++){
        if(a%i == 0){
            flag = true;
            break;
        }

    }
    if(flag == false)
        System.out.print("Prime");
    else
        System.out.print("Not Prime");
    };
}

/* NOTES
1. Why in for() loop divide by 2?
    because the factors to the input number could be possible in
    its half range
        ex: 30 factors will be possible till 15, i.e 30/2 =15,
        16 will exceed 30

2. flag is used as a variable to store the intermediate results.
Like here flag used to store a situation of  true condition.
*/
