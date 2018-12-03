interface A{  
void msgA();
}  
interface B{  
void msgB();
}  
class multiple implements A,B{
public void msgA(){System.out.println("Hello");}
public void msgB(){System.out.println("Welcome");}
public static void main(String args[]){  
   C obj=new C();  
   obj.msgA();
}  
}  