package testweb.servlet;
import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import testweb.vo.*;
import testweb.dao.UserDao;
import testweb.dao.impl.*;
public class UserLoginServlet extends HttpServlet {
	/**
	 * 
	 */
	public void doGet(HttpServletRequest req, HttpServletResponse res)
	throws IOException, ServletException{
}
	public void doPost(HttpServletRequest req, HttpServletResponse res)
	throws IOException, ServletException{
	UserInFo userinfo = new UserInFo()	;
	userinfo.setUsername(req.getParameter("username"));
	userinfo.setPassword(req.getParameter("password"));
	UserDao dao = new UserDaoImpl();
	int flag = 0;
	try {
		flag = dao.queryByUserInFo(userinfo);
		
	}
	catch (Exception e) {
		e.printStackTrace();
	}
	if(flag == 1) {
		RobotInfo robot = new RobotInfo();
        dao.SelectRobot(robot);
        
		HttpSession session=req.getSession();
		session.setAttribute("username", userinfo.getUsername());
		session.setAttribute("1", robot.getNAME());
        session.setAttribute("2", robot.getweight());
        session.setAttribute("3", robot.getiamge());
		res.sendRedirect("./welcome.jsp");
	}else {
		res.sendRedirect("./error.jsp");
	}		
	}
}
	