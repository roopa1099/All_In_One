package com.lambda.demo.test.entity;


import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@AllArgsConstructor
@NoArgsConstructor
@Setter
@Getter
public class User {


    private String userId;
    private String firstName;
    private String lastName;
    private int age;
    private Long phoneNumber;
}
