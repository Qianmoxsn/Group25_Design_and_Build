package testweb.servlet;
import java.io.IOException;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import testweb.vo.*;
import testweb.dao.UserDao;
import testweb.dao.impl.*;
import testweb.db.DBConnected;

public class UserRegistServlet extends HttpServlet {
	public void doGet(HttpServletRequest req, HttpServletResponse res)
			throws IOException, ServletException{
	}
	protected void doPost(HttpServletRequest req, HttpServletResponse res)
			throws ServletException, IOException {
		
            
		UserInFo userinfo = new UserInFo()	;
		userinfo.setUsername(req.getParameter("username"));
		userinfo.setPassword(req.getParameter("password"));  
		PreparedStatement pstmt = null ;  
            DBConnected dbc = null;
            String sql ="INSERT INTO `javawebdb`.`userinfo` (`id`, `username`, `password`) VALUES (NULL,?,?)";
            try{   
                
                dbc = new DBConnected() ;   
                pstmt = dbc.getConnection().prepareStatement(sql) ; 
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                pstmt.setString(1,userinfo.getUsername());
                pstmt.setString(2,userinfo.getPassword());
                
                
                int rs = pstmt.executeUpdate();
                  
                pstmt.close() ;
                res.sendRedirect("./welcome.jsp");
            }catch (SQLException e){   
                System.out.println(e.getMessage());   
            }finally{   
                
                dbc.close() ;   
            }
        }}
		
		
		
	
		



		