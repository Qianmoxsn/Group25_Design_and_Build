package testweb.db;
import java.sql.Connection;
import java.sql.DriverManager;
public class DBConnected {
private final String DBDRIVER = "com.mysql.cj.jdbc.Driver";
private final String DBURL = "jdbc:mysql://127.0.0.1:3306/javawebdb";
private final String DBUSER = "root";
private final String DBPASSWORD = "0000";
private Connection conn = null;
public DBConnected() {
	try {
		Class.forName(DBDRIVER);
		this.conn = DriverManager.getConnection(DBURL,DBUSER,DBPASSWORD);
	}catch (Exception e) {
		System.out.println(e.getMessage());
	}
}
public Connection getConnection() {
	return this.conn;
}
public void close() {
	try {
		this.conn.close();
	}catch (Exception e) {
}
}
}
