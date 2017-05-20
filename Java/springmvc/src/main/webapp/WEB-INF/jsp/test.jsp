<%--
  Created by IntelliJ IDEA.
  User: ly
  Date: 16/9/3
  Time: 12:25
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>test</title>
</head>
<script type="text/javascript" src="../../scripts/jquery-1.3.2.min.js"></script>
<script>
    var postData = {
        userName:123,
        age:123,
        password:123,
        id:123
    };
    $.ajax({
        cache: true,
        type: "POST",
        url: "http://localhost:8080/user/addUser",
        data: JSON.stringify(postData),
        async: false,
        success: function() {
            alert("Connection success");
        },
        error: function() {
            alert("Connection error");
        }

    });
</script>
<body>

</body>
</html>
