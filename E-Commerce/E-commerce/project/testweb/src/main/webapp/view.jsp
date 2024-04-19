<%@ page import="java.sql.DriverManager" %>
<%@ page import="java.sql.ResultSet" %>
<%@ page import="java.sql.Connection" %>
<%@ page import="java.sql.Statement" %>
<%@ page import="java.util.List" %>
<%@ page import="java.util.ArrayList" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html lang="zh-CN" style="height: 100%">
<head>
    <meta charset="utf-8">
    <style>
        #container1{
            height: 350px;
            width: 700px;
        }
        #container2{
            height: 350px;
            width: 900px;
        }
        .bao{
            text-align: center;
            font-weight: bold;
            font-size: 32px;
            margin-right: 100px;
        }
    </style>
</head>
<body style="height: 100%; margin: 0;display: flex">
<%
    String str = null, str1 = null,strs = null;
    int num = 0;
    List<String> times = new ArrayList<>();
    List<String> dates = new ArrayList<>();
    List<String> names = new ArrayList<>();
    List<Integer> nums = new ArrayList<>();
    try {
        Class.forName("com.mysql.jdbc.Driver");
        Connection con = DriverManager.getConnection("jdbc:mysql://10.129.163.203:3306/javawebdb", "root", "0000");
        Statement stmt = con.createStatement();
        Statement stmt2= con.createStatement();
        //4.执行SQL语句
        String sql = "select * from `time`";
        String sql2 = "select * from `treasure`";
        //返回ResultSet实例化对象
        ResultSet rs = stmt.executeQuery(sql);
        ResultSet rs2 = stmt2.executeQuery(sql2);
        //System.out.println("refresh");
        while (rs.next()) {
            //获取到sno字段的值
            str = rs.getString("time");
            str1 = rs.getString("date");
            times.add(str);
            dates.add(str1);
        }
        while (rs2.next()){
            strs = rs2.getString("name");
            num = rs2.getInt("num");
            names.add(strs);
            nums.add(num);
        }
        rs.close();
        rs2.close();
        //关闭操作
        stmt.close();
        stmt2.close();
        //关闭连接
        con.close();
    } catch (Exception e) {
        e.printStackTrace();
    }

%>

<div class="bao">
    <p>Average time details</p>
    <div id="container1"></div>
</div>
<div class="bao">
    <p>Treasure acquisition details</p>
    <div id="container2"></div>
</div>
<script type="text/javascript" src="https://fastly.jsdelivr.net/npm/echarts@5.4.2/dist/echarts.min.js"></script>
<script type="text/javascript">
    var dom1 = document.getElementById('container1');
    var dom2 = document.getElementById('container2');
    var myChart = echarts.init(dom1, null, {
        renderer: 'canvas',
        useDirtyRect: false
    });
    var myChart2 = echarts.init(dom2, null, {
        renderer: 'canvas',
        useDirtyRect: false
    });
    var app = {};
    var option;
    var option2;
    var dataList = new Array();
    var nameList = new Array();
    console.log("ooo")
    
    <%   for(int i=0;i <dates.size();i++){   %>
    dataList[<%=i%>] = "<%=dates.get(i)%>";
    <%   }   %>
    <%   for(int i=0;i <names.size();i++){   %>
    nameList[<%=i%>] = "<%=names.get(i)%>";
    <%   }   %>
    
    
    option = {
        tooltip:{
          trigger:"item",
            formatter: "{c}s"
        },
        xAxis: {
            type: 'category',
            data: dataList
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                data: <%= times%>,
                type: 'line'
            }
        ]
    };
    option2 = {
        tooltip:{
            trigger:"item",
            formatter: "{c}piece"
        },
        xAxis: {
            type: 'category',
            data:nameList
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                data: <%= nums%>,
                type: 'bar'
            }
        ]
    };
    console.log(option);
    console.log(option2);
    if (option && typeof option === 'object') {
        myChart.setOption(option);
    }
    if (option2 && typeof option2 === 'object') {
        myChart2.setOption(option2);
    }
    window.addEventListener('resize', myChart.resize);
    window.addEventListener('resize', myChart2.resize);
   
               

</script>
</body>
</html>