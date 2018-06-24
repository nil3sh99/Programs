#include<conio.h>
#include<iostream>

using namespace std;

long fact(int n){

	if(n==0)
		return 1;

		return( n*fact(n-1));
}

int main(){
	int num;
	cout<<"Enter the number whose fact is required";
	cin>> num;
	cout<<"Fact of "<<num<<"is"<< fact(num);

getch();
return 0;
}
