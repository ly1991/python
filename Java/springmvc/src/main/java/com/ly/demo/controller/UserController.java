package com.ly.demo.controller;

import com.ly.demo.model.User;
import com.ly.demo.service.UserService;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import javax.annotation.Resource;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.*;

/**
 * TODO
 * Created by ly on 16/4/21.
 */
@Controller
@RequestMapping("/user")
public class UserController {
    @Resource
    private UserService userService;


    @RequestMapping("/addUser")
    public ModelAndView addUser(HttpServletRequest request){
        String id = request.getParameter("id");
        String userName = request.getParameter("userName");
        String password = request.getParameter("password");
        String age = request.getParameter("age");
        User user = new User();
        user.setId(Integer.parseInt(id));
        user.setUserName(userName);
        user.setPassword(password);
        user.setAge(Integer.parseInt(age));
        userService.addUser(user);
        List<User> users = userService.getAllUser();
        ModelAndView mv = new ModelAndView("showUser");
        mv.addObject("users",users);
        return  mv;
    }

    @RequestMapping("/getUserByID")
    public ModelAndView getUserByID(HttpServletRequest request){
        User user = userService.getUserByID(Integer.parseInt(request.getParameter("id")));
        ModelAndView mv = new ModelAndView("userInfo");
        mv.addObject("user",user);
        return mv;
    }

    @RequestMapping("/showUser")
    public ModelAndView getAllUser(){
        List<User> users = userService.getAllUser();
        ModelAndView mv = new ModelAndView("showUser");
        mv.addObject("users",users);
        return mv;
    }
    @RequestMapping("/deleteUser")
    public ModelAndView deleteUser(HttpServletRequest request){
        String id = request.getParameter("id");
        userService.deleteUser(Integer.parseInt(id));
        List<User> users = userService.getAllUser();
        ModelAndView mv = new ModelAndView("showUser");
        mv.addObject("users",users);
        return  mv;
    }

    @RequestMapping("/updateUser")
    public ModelAndView updateUser(HttpServletRequest request){
        String id = request.getParameter("id");
        String userName = request.getParameter("userName");
        String password = request.getParameter("password");
        String age = request.getParameter("age");
        User user = new User();
        user.setId(Integer.parseInt(id));
        user.setUserName(userName);
        user.setPassword(password);
        user.setAge(Integer.parseInt(age));
        userService.updateUser(user);
        List<User> users = userService.getAllUser();
        ModelAndView mv = new ModelAndView("showUser");
        mv.addObject("users",users);
        return  mv;
    }

    //页面跳转
    @RequestMapping("/page")
    public ModelAndView send(HttpServletRequest request){
        String page = request.getParameter("page");
        return new ModelAndView(page);
    }
}
