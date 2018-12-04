class excep1{
//	static int i;
	static void valid(int age){
		
		if(age<18){
			throw new ArithmeticException("Can not vote");
		}
		else{
			System.out.println("Welcome");
		}
	}
	public static void main(String ar[]){
		
		try{
			valid(Integer.parseInt(ar[0]));
		}
		catch(ArithmeticException ae){
			System.out.println(ae);
		}
		finally{
			System.out.println("Welcome to testing!!");
		}
	
	}
}