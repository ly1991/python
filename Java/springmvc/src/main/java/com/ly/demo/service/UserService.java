package com.ly.demo.service;

import com.ly.demo.model.User;

import java.util.List;

/**
 * TODO
 * Created by ly on 16/4/20.
 */
public interface UserService {
     void addUser(User user);
     User getUserByID(int id);
     List<User> getAllUser();
     void deleteUser(int id);
     void updateUser(User user);
}

