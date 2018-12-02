### Introduction to JDBC

Java JDBC is an API to connect and execute query with the database.

#### Steps for connection :-
1. Register driver class

```java
Class.forName("oracle.jdbc.OracleDriver");
```

2. Creating a connection

```java
Connection con = DriverManager.getConnection("//path"; "username"; "pass");
```

3. Creating statement object

Statement object will execute the database queries
```java
Statement stmt = con.createStatement();
```

4. Execute Query

```java

Result rs = stmt.executeQuery("select * from EMP");
while (rs.next())
rs.getInt(); // rs.getString() if the input to take is a string type
```

5. Closing a connection

``` con.close()```


Summary of steps we did for creating a connection:-

1.Register the class with driver (Class.forName("specifications of your database"))
2.Creating a connection object (Connection con = getConnection("1";"2";"3"))
3.Create a statement object (Statement stmt = con.createStatement())
4.Execute a query (Result rs = stmt.executeQuery("Your query here"))
5.Close the connection (con.close())

#### Lecture-1