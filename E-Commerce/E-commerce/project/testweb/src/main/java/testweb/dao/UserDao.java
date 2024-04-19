package testweb.dao;
import testweb.vo.*;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.SQLException;
import testweb.dao.UserDao;
import testweb.vo.UserInFo;

public interface UserDao {
public int queryByUserInFo (UserInFo userinfo) throws Exception;
public void SelectRobot(RobotInfo robot);	

}
