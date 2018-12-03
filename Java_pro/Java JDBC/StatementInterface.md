## Statement Interface

Provides a method to execute the database queries with the database

### Methods:-
1) executeQuery(String sql)
	Generates an output which is stored in a java object like:: 
```java
Result rs = stmt.executeQuery("select * from emp");
```

2) executeUpdate()
	Used for insertion, updation and deletion from a database

3) execute(String sql)
	Boolean value

4) executeBatch()
	When there are multiple insert, update or alike queries, then handling of these multiple queries is done by this.


Example:-

```java
import java.sql.*;

class sql1{
	public static void main(String ar[]){
		Class.forName("oracle.jdbc.driver.OracleDriver");
		Connection con = DriverManager.getConnection("jdbc:mysql:/localHost:8080/Emp");
		Statement stmt = con.createStatement();
		Result rs = stmt.executeQuery("select * from Emp");
		int i = stmt.executeUpdate("delete from emp where id=1");
		while(rs.next()){
			System.out.println(rs.getInt(1));
			System.out.println(rs.getString(2));
		}
		rs.close();
	}
		con.close();
}

```

#### For any queries open an Issue :D
#### For any update generate a PR ;)