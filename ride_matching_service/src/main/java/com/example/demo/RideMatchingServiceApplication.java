package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import io.github.cdimascio.dotenv.Dotenv;

@SpringBootApplication
public class RideMatchingServiceApplication {

    public static void main(String[] args) {
    	
    	
//    	Dotenv dotenv = Dotenv.load();
    	Dotenv dotenv = Dotenv.configure().filename(".env.dev").load();
        System.setProperty("DB_USERNAME", dotenv.get("DB_USERNAME"));
        System.setProperty("DB_PASSWORD", dotenv.get("DB_PASSWORD"));
        System.setProperty("DB_NAME", dotenv.get("DB_NAME"));
        
        
        SpringApplication app = new SpringApplication(RideMatchingServiceApplication.class);
        app.setBanner((environment, sourceClass, out) -> out.println("Welcome to Ride Matching Service!"));
        app.run(args);
    }

}
