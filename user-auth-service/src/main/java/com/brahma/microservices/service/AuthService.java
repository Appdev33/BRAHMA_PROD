package com.brahma.microservices.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import com.brahma.microservices.model.AuthUser;

import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.security.Keys;

import java.nio.charset.StandardCharsets;
import java.util.*;

import javax.crypto.SecretKey;

import org.springframework.util.*;


@Service
public class AuthService {

    private static final String SECRET_KEY = "your_secret_key_with_sufficient_length";
    private Map<String, AuthUser> userMap = new HashMap<>(); // In-memory storage

    @Autowired
    private RestTemplate restTemplate;

//    @Value("${registration.service.url}")
    private String registrationServiceUrl;

	    public String register(String username, String password, String role) {
	        // Save the user to the in-memory storage (auth-service)
	        AuthUser authUser = new AuthUser(username, password, role);
	        userMap.put(username, authUser);
	
	        // Generate a JWT token with the user's details
	        return generateToken(username, role);
	    }

    public String login(String username, String password) {
        // Validate credentials (in a real-world scenario, you might check the in-memory storage)
        AuthUser authUser = userMap.get(username);

        if (authUser != null && authUser.getPassword().equals(password)) {
            // Generate a JWT token with the user's details
            return generateToken(authUser.getUsername(), authUser.getRole());
        } else {
            return null; // Invalid credentials
        }
    }

    private String generateToken(String username, String role) {
        byte[] secretKeyBytes = SECRET_KEY.getBytes(StandardCharsets.UTF_8); // Assuming SECRET_KEY is a String
        SecretKey secretKey = Keys.hmacShaKeyFor(secretKeyBytes);


        return Jwts.builder()
                .setSubject(username)
                .claim("role", role)
                .signWith(secretKey) // Updated signing method
                .compact();
    }
}

