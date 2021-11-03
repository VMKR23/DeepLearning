import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Query {
  public static void queryAll(Connection con)
    {
    PreparedStatement ps=null;
    ResultSet rs=null;
    String sql="SELECT * from Movies";
    try {
      ps=con.prepareStatement(sql);
      rs=ps.executeQuery();
      System.out.println("name         Actor        Actress             Director            Year");
      while(rs.next())
      {
        String name=rs.getString(1);
        while(name.length()!=15)
        {
          name=name.concat(" ");
        }
        String actor=rs.getString(2);
        while(actor.length()!=15)
        {
          actor=actor.concat(" ");
        }
        String actress=rs.getString(3);
        while(actress.length()!=20)
        {
          actress=actress.concat(" ");
        }
        String director=rs.getString(4);
        while(director.length()!=20)
        {
          director=director.concat(" ");
        }
        int year=rs.getInt(5);
        System.out.println(name+""+actor+""+actress+""+director+""+year);
      }
    } catch (SQLException e) {
      System.out.println(e);
    }
    }
  public static void querybyactor(Connection con,String actor)
    {
    String sql="SELECT name FROM Movies Where actor = ?";
    ResultSet rs=null;
    PreparedStatement ps=null;
    try {
      ps=con.prepareStatement(sql);
      ps.setString(1,actor);
      rs=ps.executeQuery();
      while(rs.next())
      {
        System.out.println(rs.getString(1));
      }
    } catch (SQLException e) {
      System.out.println(e);
    }
    }
}