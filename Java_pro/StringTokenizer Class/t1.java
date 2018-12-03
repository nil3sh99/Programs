import java.util.StringTokenizer;

class t1{
	public static void main(String ar[]){
		StringTokenizer st = new StringTokenizer("my name is khan", " ");
		while(st.hasMoreTokens()){System.out.println(st.nextToken());}
	}
}