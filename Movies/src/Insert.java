import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class Insert {
   public static void insert(Connection con,String name,String actor,String actress,String director,int year)
    {
     PreparedStatement ps=null;
     try
     {
       String sql="Insert into Movies(name,actor,actress,director,year) VALUES(?,?,?,?,?)";
       ps=con.prepareStatement(sql);
       ps.setString(1,name);
       ps.setString(2,actor);
       ps.setString(3,actress);
       ps.setString(4,director);
       ps.setInt(5,year);
       ps.execute();
      System.out.println("Record Inserted Successfully"); 
     }
     catch(SQLException e)
     {
       System.out.println(e);
     }
    }
   
}