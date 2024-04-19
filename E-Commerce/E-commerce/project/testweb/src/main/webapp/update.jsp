<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<%
    String id = request.getParameter("id");
    String weight = request.getParameter("weight");
    String size = request.getParameter("size");
    String image = request.getParameter("image");
%>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
     <form action="./wy" method="post">
        <label>id:</label>
        <input name="id" value="<%= id%>">
        <br>
        <label>weight:</label>
        <input name="weight" value="<%= weight%>">
        <br>
        <label>size:</label>
        <input name="size" value="<%= size%>">
        <br>
        <label>image:</label>
        <input name="image" value="<%= image%>">
        <br>
        <button type="submit">submit</button>
      </form>
</body>
</html>