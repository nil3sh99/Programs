## Connecting with different databases

### Oracle Database

Driver class = oracle.driver.OracleDriver
Connection url = jdbc:oracle:this@localhost:Port_number:xe

Ex:-
```java
import java.sql.*;

class sql1{
	public static void main(String ar[]){
		try {
			Class.forName("oracle:driver:OracleDriver"; "UserName"; "Password");
			Connection con = DriverManager.getConnection(url);
			Statement stmt = con.createStatement();
			}
	}
}
```

### MySQL

only the driver class changes, rest process remains same and hence:-

Driver class = con.mysql.jdbc.Driver
Connection url = jdbc:mysql://localhost:8080:DatabaseName;


### Access database

Two types are possible in this (1) With DSN    (2)Without DSN
				Data Source Name