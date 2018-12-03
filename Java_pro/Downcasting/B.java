class A{
	void fun1(){
		System.out.println("Hello i am from A");
	}
}

class B extends A{
	void fun1(){
		System.out.println("Hello i am from B");
	}
public static void main(String ar[]){
//		A a = new B();  	// Upcasting works ... dynamic method dispatch
		B b = (B) new A();	// downcasting Compile Time Error
		b.fun1();
	}
}	