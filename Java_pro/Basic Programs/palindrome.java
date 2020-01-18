class palindrome{
    public static void main(String args[]){
        int a = 121;
        int sum =0,res =0;
        while(a>0){
            sum = a%10;
            res = sum + (10*res);
            a = a/10;
        }
        if(res == a){
            System.out.print("Palindrome");
        }
        else
            System.out.print("Not Palindrome");
    };
}
