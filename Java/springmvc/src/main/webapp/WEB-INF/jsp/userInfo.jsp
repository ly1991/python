<%--
  Created by IntelliJ IDEA.
  User: ly
  Date: 16/5/8
  Time: 17:25
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>修改</title>
</head>
<body>
    <form action="${pageContext.request.contextPath}/user/updateUser">
        <table>
            <tr>
                <td>姓名:</td>
                <td><input type="text" value="${user.userName}" name="userName"></td>
            </tr>
            <tr>
                <td>密码:</td>
                <td><input type="text" value="${user.password}" name="password"></td>
            </tr>
            <tr>
                <td>年龄:</td>
                <td><input type="text" value="${user.age}" name="age"></td>
            </tr>
            <tr>
                <td>ID:</td>
                <td><input type="text"  value="${user.id}" name="id"></td>
            </tr>
            <tr><td><input value="确认修改" type="submit"/></td></tr>
        </table>
    </form>
</body>
</html>
