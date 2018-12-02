## Introduction

At times, it is necessary to use native (non-Java) codes (e.g., C/C++) to overcome the memory management and performance constraints in Java. Java supports native codes via the Java Native Interface (JNI).

JNI is difficult, as it involves two languages and runtimes.

I shall assume that you are familiar with:
1. Java.
2. C/C++ and the GCC Compiler (Read "GCC and Make").

### Code

1. Java source code:-

```
public class HelloJNI{
	static{
		System.loadLibrary("native");
	}
}
	private native void Hello(); //Method of a native class, define its function using native code (C/C++)

	public static void main(String args[]){
		new HelloJNI().Hello();
	}
}
```

2. C source code

```
#include<stdio.h>
#include<jni.h>
#include "HelloJNI" // library that you made in your java code

JNIEXPORT void JNICALL Java_HelloJNI_Hello(JNIEnv *env, jObject thisObj){
	printf("Hello there! Thanks for using the repository!! :D");
	return;
}
```