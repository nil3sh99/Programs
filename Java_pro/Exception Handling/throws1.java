class myexcep extends Exception{
	myexcep(String s){
		super(s);
	}
}

class throws1{ 
	static void validage(int age) throws myexcep{
		if(age<18){
			throw new myexcep("Not a valid age");
		}
		else{
		}

	}
	public static void main(String ar[]){
		try{
			validage(Integer.parseInt(ar[0]));
		}
		catch(Exception e){
			System.out.println(e);
		}
	}
}