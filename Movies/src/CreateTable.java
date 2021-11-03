import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;

public class CreateTable {
	public static void createTable(Connection con)
	  {
	    String sql="create table Movies(name Varchar2(15),actor Varchar2(15),actress Varchar2(15),director Varchar2(15),year Number(4))";
	    Statement stmt;
	  try {
	    stmt = con.createStatement();
	    stmt.executeUpdate(sql);
	  } catch (SQLException e) {
	    System.out.println(e);
	  }
	    
	    System.out.println("Table created Successfully");
}
}
