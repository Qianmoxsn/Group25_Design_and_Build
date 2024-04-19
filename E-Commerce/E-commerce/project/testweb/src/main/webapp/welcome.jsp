<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to Robot World!</title>
  
</head>
<body>
    <%String username = (String)session.getAttribute("username"); %>
   <%String NAME = (String)session.getAttribute("1"); %>
   <%String WEIGHT = (String)session.getAttribute("2"); %>
   <%String IMAGE = (String)session.getAttribute("3"); %>
    welcome   <%= username %>
    welcome   <%= NAME %>
    welcome   <%= WEIGHT %>
    welcome   <%= IMAGE %>
    <h1>Welcome to Robot World!</h1>
    
    <h2>Robot Information</h2>
    <a href = "view.jsp">view</a>
    <a href = "add.jsp">add</a>
    <a href = "update.jsp">update</a>
    
    <div>.

    </div>.
    <div class="abc">
        <label>Name: </label>
        <span id="robotName"><%= NAME %></span>
    </div>
    <div class="wyy">
        <label>Size: </label>
        <span id="robotSize">Medium</span>
    </div>
    <div>
        <label>Weight: </label>
        <span id="robotWeight"><%= WEIGHT %> kg</span>
    </div>
    
<button id="openbtn">Add a new robot </button>
<div class="overlay" id="overlay"></div>
<div class="popup" id="popup">
<form method="post" action="./wy">
    <input type="hidden" name="action" value="addRobot">
    <label>NAME:</label>
    <input type="text" value="" name ="robotname" placeholder="please input NAME"/><br><br>
    <label>WEIGHT:</label>
    <input type="text" value="" name ="robotweight" placeholder="please input WEIGHT" /><br><br>
    <label>SIZE:</label>
    <input type="text" value="" name="robotsize"  placeholder="please input SIZE" /><br><br>
    <button id="closebtn()">CLOSE</button>
    <button type="submit">Submit</button>
</form>
</div>
