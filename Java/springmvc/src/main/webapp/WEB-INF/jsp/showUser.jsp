<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page language="java"  pageEncoding="utf-8"%>
<html>
  <head>
	<title>测试</title>
  </head>
  <body>
      <div align="center">
      用户列表<br>
        <table>
            <tr>
                <td>姓名</td>
                <td>密码</td>
                <td>年龄</td>
                <td>ID</td>
            </tr>
          <c:forEach items="${users}" var="user">
            <tr>
                <td>${user.userName}</td>
                <td>${user.password}</td>
                <td>${user.age}</td>
                <td>${user.id}</td>
                <td><a href="<%=request.getContextPath()%>/user/getUserByID?id=${user.id}">修改</a></td>
                <td><a href="<%=request.getContextPath()%>/user/deleteUser?id=${user.id}">删除</a></td>
            </tr>
          </c:forEach>
            <tr>
                <td><a href="<%=request.getContextPath()%>/user/page?page=addUser"><button>增加用户</button></a></td>
            </tr>

        </table>


      </div>
  </body>
</html>
