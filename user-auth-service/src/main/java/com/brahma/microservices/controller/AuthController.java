package com.brahma.microservices.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.brahma.microservices.model.AuthUser;
import com.brahma.microservices.service.AuthService;


@RestController
@RequestMapping("/api/auth")
public class AuthController {

    private final AuthService authService;

    @Autowired
    public AuthController(AuthService authService) {
        this.authService = authService;
    }
    
	  @GetMapping("/all")
	  public ResponseEntity<String> getAllUsers() {
		  return new ResponseEntity<>("token", HttpStatus.OK); 
	  }
    
    @PostMapping("/register")
    public ResponseEntity<String> register(@RequestParam String username, @RequestParam String password) {
        // Register the user and return a JWT token
        String token = authService.register(username, password, "USER");
        
        return new ResponseEntity<>(token, HttpStatus.CREATED);
        
//        if (token != null) {
//            return new ResponseEntity<>(token, HttpStatus.CREATED);
//        } else {
//            return new ResponseEntity<>("Registration failed", HttpStatus.BAD_REQUEST);
//        }
    }

    @PostMapping("/login")
    public ResponseEntity<String> login(@RequestBody AuthUser authUser) {
        // Authenticate the user and return a JWT token
        String token = authService.login(authUser.getUsername(), authUser.getPassword());

        if (token != null) {
            return new ResponseEntity<>(token, HttpStatus.OK);
        } else {
            return new ResponseEntity<>("Invalid credentials", HttpStatus.UNAUTHORIZED);
        }
    }
}


