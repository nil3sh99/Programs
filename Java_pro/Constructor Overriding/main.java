class student{
	 int id;
	 int roll_no;
	 String name;	
	
	student(int i, String s){
	id = i;
	name = s;
	}
	student(int i, String s, int r){
	id = i;
	name = s;
	roll_no = r;
	}
	void display(){
		System.out.println(id + name + roll_no);
	}
}

class main{
	public static void main(String ar[]){
	student s1 = new student(1, "A");
	student s2 = new student(2, "B", 201);
	//System.out.println(id + name + roll_no);
	s1.display();
//	s2.display();
	}
}