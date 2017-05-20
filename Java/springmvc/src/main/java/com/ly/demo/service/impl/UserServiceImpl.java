package com.ly.demo.service.impl;

import com.ly.demo.dao.UserDao;
import com.ly.demo.model.User;
import com.ly.demo.service.UserService;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.List;

/**
 * TODO
 * Created by ly on 16/4/20.
 */
@Service("userService")
public class UserServiceImpl implements UserService{
    @Resource
    private UserDao userDao;

    @Override
    public void addUser(User user){
        userDao.addUser(user);
    }

    @Override
    public List<User> getAllUser(){
        return userDao.getAllUser();
    }

    @Override
    public void deleteUser(int id) {
        userDao.deleteUser(id);
    }

    @Override
    public User getUserByID(int id){
        return userDao.getUserByID(id);
    }

    @Override
    public void updateUser(User user){
        userDao.updateUser(user);
    }
}
