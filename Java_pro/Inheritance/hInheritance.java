class A{
	void eat(){
		System.out.println("i eat");
	}
}

class B extends A{
	void bark(){
		System.out.println("Dog barks");
	}
}

class C extends A{
	void speak(){
		System.out.println("Humans speak");
	}
}

class hInheritance{
	public static void main(String[] ar) {
		B b = new B();
		C c = new C();
		b.bark();
		b.eat();
		c.eat();
	}
}