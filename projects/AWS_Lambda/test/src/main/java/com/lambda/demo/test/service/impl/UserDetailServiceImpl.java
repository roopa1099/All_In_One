package com.lambda.demo.test.service.impl;

import com.lambda.demo.test.entity.User;
import com.lambda.demo.test.service.UserDetailService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.*;

@Slf4j
@Service
public class UserDetailServiceImpl implements UserDetailService {

    private final List<User> userList = new ArrayList<>();


    @Override
    public void addUser(User user) {
        if(user.getFirstName().isBlank()){
            log.error("First name is missing.");
            throw new RuntimeException("Invalid user info.");
        }
        user.setUserId(UUID.randomUUID().toString());

        userList.add(user);
    }

    @Override
    public Optional<User> getUser(String id) {
        Optional<User> user = userList.stream().filter((userInfo)->userInfo.getUserId().equals(id)).findFirst();
        return user;
    }

    @Override
    public List<User> listUsers() {

        return userList;
    }
}
