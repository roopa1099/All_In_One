package com.lambda.demo.test.service;


import com.lambda.demo.test.entity.User;

import java.util.List;
import java.util.Optional;

public interface UserDetailService {

    void addUser(User user);

    Optional<User> getUser(String id);

    List<User> listUsers();

}
