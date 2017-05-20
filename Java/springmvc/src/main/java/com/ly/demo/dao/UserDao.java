package com.ly.demo.dao;

import com.ly.demo.model.User;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * TODO
 * Created by ly on 16/4/20.
 */
@Repository
public interface  UserDao {

    void addUser(User user);
    User getUserByID(int id);
    List<User> getAllUser();
    void deleteUser(int id);
    void updateUser(User user);

}
