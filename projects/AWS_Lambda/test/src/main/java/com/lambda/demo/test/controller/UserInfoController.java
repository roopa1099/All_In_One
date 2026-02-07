package com.lambda.demo.test.controller;

import com.lambda.demo.test.entity.User;
import com.lambda.demo.test.service.UserDetailService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
public class UserInfoController {

    @GetMapping("/")
    public String welcome() {
        return "Application is UP and running!";
    }

    @Autowired
    UserDetailService userDetailService;

    @PostMapping("/user")
    public void addUser(@RequestBody  User user){
        userDetailService.addUser(user);
    }

    @GetMapping("/user/{userId}")
    public Optional<User> getUser(@PathVariable String userId){
        return userDetailService.getUser(userId);
    }

    @GetMapping("/users")
    public List<User> getUsers(){
        return userDetailService.listUsers();
    }




}
