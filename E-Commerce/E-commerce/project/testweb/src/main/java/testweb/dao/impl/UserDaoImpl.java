package testweb.dao.impl;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import testweb.db.DBConnected;
import testweb.dao.UserDao;
import testweb.vo.RobotInfo;
import testweb.vo.UserInFo;

public class UserDaoImpl implements UserDao {

	@Override
	public int queryByUserInFo(UserInFo userinfo) throws Exception {
		int flag = 0;
		String sql = "select * from userinfo where username=?";
		PreparedStatement pstmt = null;
		DBConnected dbc = null;
		try {
			dbc = new DBConnected();
			pstmt = dbc.getConnection().prepareStatement(sql);
			pstmt.setString(1,userinfo.getUsername());
			ResultSet rs = pstmt.executeQuery();
			while(rs.next()) {
				if(rs.getString("password").equals(userinfo.getPassword())) {
				flag = 1;
			}
		}
		rs.close();
		pstmt.close();}
	catch (SQLException e) {
		System.out.println(e.getMessage());}
	finally {dbc.close();}
		// TODO Auto-generated method stub
		return flag;
	}
	public void SelectRobot(RobotInfo Robot){
		
		String sql = "select * from Robot where id=?";
        PreparedStatement pstmt = null ;   
        DBConnected dbc = null;   
  
        try{   
            // 连接数据库   
            dbc = new DBConnected() ;   
            pstmt = dbc.getConnection().prepareStatement(sql) ; 
            pstmt.setInt(1,1) ;   
            // 进行数据库查询操作   
            ResultSet rs = pstmt.executeQuery();
            while(rs.next()){  
                // 查询出内容，将其与用户提交的内容对比 
                Robot.setid(rs.getString("id"));
                Robot.setweight(rs.getString("weight"));
                Robot.setsize(rs.getString("size"));
                Robot.setimage(rs.getString("image"));
            }   
            rs.close() ; 
            pstmt.close() ;   
        }catch (SQLException e){   
            System.out.println(e.getMessage());   
        }finally{   
            // 关闭数据库连接   
            dbc.close() ;   
        }   
	}
}
