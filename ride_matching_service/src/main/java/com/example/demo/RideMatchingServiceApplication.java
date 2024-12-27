package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class RideMatchingServiceApplication {

    public static void main(String[] args) {
        SpringApplication app = new SpringApplication(RideMatchingServiceApplication.class);
        app.setBanner((environment, sourceClass, out) -> out.println("Welcome to Ride Matching Service!"));
        app.run(args);
    }

}
