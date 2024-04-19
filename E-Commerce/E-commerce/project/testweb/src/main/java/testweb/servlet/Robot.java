package testweb.servlet;

import java.io.IOException;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import testweb.db.*;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import testweb.db.DBConnected;
import testweb.vo.*;
/**

 */
@WebServlet("/welcome")
public class Robot extends HttpServlet {
	protected void doPost(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
		String action = req.getParameter("action");

        if ("addRobot".equals(action)) {
            
        	RobotInfo robot =new RobotInfo();
            robot.setid(req.getParameter("id"));
            robot.setweight(req.getParameter("weight"));
            robot.setsize(req.getParameter("size"));
            PreparedStatement pstmt = null ;   
            DBConnected dbc = null;
            String sql ="INSERT INTO `javawebdb`.`robot` (`id`, `weight`, `size`, `image`) VALUES (NULL,?,?,?,NULL)";
            try{   
                
                dbc = new DBConnected() ;   
                pstmt = dbc.getConnection().prepareStatement(sql) ; 
                pstmt.setString(1,robot.getid());
                pstmt.setString(2,robot.getweight());
                pstmt.setString(3,robot.getsize());
                
                int rs = pstmt.executeUpdate();
                  
                pstmt.close() ;
                res.sendRedirect("./welcome.jsp");
            }catch (SQLException e){   
                System.out.println(e.getMessage());   
            }finally{   
                
                dbc.close() ;   
            }
        } else if ("deleteRobot".equals(action)) {
        	 
        	RobotInfo robot =new RobotInfo();
            String id =req.getParameter("robotid");
        	PreparedStatement pstmt = null ;   
            DBConnected dbc = null;
            String sql ="DELETE FROM Robot WHERE id = ?";
;
            try{   
                 
                dbc = new DBConnected() ;   
                pstmt = dbc.getConnection().prepareStatement(sql) ; 
                pstmt.setString(1,id);
                
                int rs = pstmt.executeUpdate();
                  
                pstmt.close() ; 
                res.sendRedirect("./welcome.jsp");
            }catch (SQLException e){   
                System.out.println(e.getMessage());   
            }finally{   
                 
                dbc.close() ;   
            }
        } else if ("changeRobot".equals(action)) {
        	RobotInfo robot =new RobotInfo();
        	String id =req.getParameter("id");
            robot.setid(req.getParameter("id"));
            robot.setweight(req.getParameter("weight"));
            robot.setsize(req.getParameter("size"));
            PreparedStatement pstmt = null ;   
            DBConnected dbc = null;
            String sql ="UPDATE Robot SET weight = ?, size=? WHERE id =?";
;
            try{   
                  
                dbc = new DBConnected() ;   
                pstmt = dbc.getConnection().prepareStatement(sql) ; 
                pstmt.setString(1,robot.getid());
                pstmt.setString(2,robot.getweight());
                pstmt.setString(3,robot.getsize());
                pstmt.setString(4, id);
                
                int rs = pstmt.executeUpdate();
                pstmt.close() ; 
                res.sendRedirect("./welcome.jsp");
            }catch (SQLException e){   
                System.out.println(e.getMessage());   
            }finally{   
                
                dbc.close() ;
            
        }
         }
	}
}
            
