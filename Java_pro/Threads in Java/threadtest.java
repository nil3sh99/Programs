// using interface

class t1 implements Runnable{
	public void run(){
	for(int i=0; i<=5; i++)
		System.out.println(i);
	}
}

class t2 implements Runnable{
	public void run(){
	for(int j=0; j<=5; j++)
		System.out.println(j);
	}
}

class threadtest {
	public static void main(String ar[]){
		t1 t11 = new t1();
		t2 t22 = new t2();
		Thread thread1 = new Thread(t11);
		Thread thread2 = new Thread(t22);
		thread1.start();
		thread2.start();
	}
}
