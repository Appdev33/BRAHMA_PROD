package com.brahma.microservices.controller;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestClientException;
import org.springframework.web.client.RestTemplate;
import org.springframework.util.*;
import com.brahma.microservices.model.User;
import com.brahma.microservices.service.RegistrationService;

//@RestController
//@RequestMapping("/api/registration")
//public class RegistrationController {
//
//    @Autowired
//    private RegistrationService registrationService;
//
//    @PostMapping("/users")
//    public ResponseEntity<String> registerUser(@RequestBody User toBeAdded) {
//        registrationService.registerNewUser(toBeAdded);
//        return new ResponseEntity<>("User registered successfully", HttpStatus.CREATED);
//    }
//
//    @GetMapping("/users/{id}")
//    public ResponseEntity<Optional<User>> getUserById(@PathVariable Long id) {
//        Optional<User> userDto = registrationService.findUserById(id);
//        return ResponseEntity.ok(userDto);
//    }
//}

@RestController
@RequestMapping("/api/users")
public class RegistrationController {

    private final RegistrationService registrationService;
    private final RestTemplate restTemplate;
    private final EventProducer eventProducer;

    @Autowired
    public RegistrationController(RegistrationService registrationService, RestTemplate restTemplate, EventProducer eventProducer) {
        this.registrationService = registrationService;
        this.restTemplate = restTemplate;
        this.eventProducer = eventProducer;
    }

    @PostMapping("/add")
    public ResponseEntity<String> addUser(@RequestParam String username, @RequestParam String password) {
        // Onboard user in the registration service
        registrationService.onboardUser(username, password);
        
        // Make a call to auth-service to register the user
        String authUrl = "http://localhost:8442/api/auth/register";
        String notificationServiceUrl = "http://127.0.0.1:5000/events/create"; // URL of the notification service endpoint


        // Pass only necessary information for registration
        MultiValueMap<String, String> requestBody = new LinkedMultiValueMap<>();
        requestBody.add("username", username);
        requestBody.add("password", password);
        
        String event = "{\"username\": \"" + username + "\", \"action\": \"register\"}";
//        eventProducer.publishEvent("hello-topic", event);  --this is working kafka code
        
        // Make the registration request to auth-service
        try {
            ResponseEntity<String> authResponse = restTemplate.postForEntity(authUrl, requestBody, String.class);
            
            // Send notification to the user
            if (authResponse.getStatusCode() == HttpStatus.CREATED) {
                event = "{\"event_type\": \"user_registration\", \"payload\": {\"username\": \"" + username + "\", \"message\": \"Welcome to our platform!\"}}";
                HttpHeaders headers = new HttpHeaders();
                headers.setContentType(MediaType.APPLICATION_JSON);
                HttpEntity<String> eventEntity = new HttpEntity<>(event, headers);
                ResponseEntity<String> notificationResponse = restTemplate.postForEntity(notificationServiceUrl, eventEntity, String.class);
                
                if (notificationResponse.getStatusCode() == HttpStatus.CREATED) {
                    return new ResponseEntity<>("User registered successfully and notification sent", HttpStatus.CREATED);
                } else {
                    return new ResponseEntity<>("User registered successfully but failed to send notification", HttpStatus.INTERNAL_SERVER_ERROR);
                }
            } else {
                return new ResponseEntity<>("User registration failed in auth-service", HttpStatus.INTERNAL_SERVER_ERROR);
            }
        } catch (RestClientException e) {
            return new ResponseEntity<>("Error making request to Auth Service or Notification Service", HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
        
        // Make the registration request to auth-service
//        try {
//            // Make the registration request to auth-service
//            ResponseEntity<String> authResponse = restTemplate.postForEntity(authUrl, requestBody, String.class);
//            // Process the response...
//        } catch (Exception e) {
//            System.out.print("Error making request to Auth Service");
//            // Handle the exception...
//        }
        
//        ResponseEntity<String> authResponse = restTemplate.postForEntity(authUrl, requestBody, String.class);
//        return new ResponseEntity<String>("User registered successfully"+authResponse, HttpStatus.CREATED);
////        if (authResponse.getStatusCode() == HttpStatus.CREATED) {
//            // Registration successful in both services
//            return new ResponseEntity<>("User registered successfully", HttpStatus.CREATED);
//        } else {
//            // Registration failed in auth-service
//            return new ResponseEntity<>("User registration failed in auth-service", HttpStatus.INTERNAL_SERVER_ERROR);
//        }
    
	    
    
	  @GetMapping("/find/{userId}")
	  public ResponseEntity<String> findUserById(@PathVariable Long userId) {
	  	User user = registrationService.getUserById(userId);
	  	return Optional.ofNullable(user)
	  	        .map(u -> new ResponseEntity<>("User found" + u.getUsername(), HttpStatus.OK))
	  	        .orElse(new ResponseEntity<>("User not found", HttpStatus.NOT_FOUND));
	
	  }
	
	  @GetMapping("/all")
	  public List<User> getAllUsers() {
	      return registrationService.getAllUsers();
	  }

    // Other methods...
}


//@RestController
//@RequestMapping("/api/users")
//public class RegistrationController {
//
//    private final RegistrationService registrationService;
//    
//    private final RestTemplate restTemplate;
//
//    @Autowired
//    public RegistrationController(RegistrationService registrationService) {
//        this.registrationService = registrationService;
//    }
//
//    @PostMapping("/add")
//    public ResponseEntity<String> addUser(@RequestParam String username, @RequestParam String password) {
//    	
//    	registrationService.onboardUser(username, password);
//    	return new ResponseEntity<String>("User registered successfully", HttpStatus.CREATED);
//    }
//
//    @GetMapping("/find/{userId}")
//    public ResponseEntity<String> findUserById(@PathVariable Long userId) {
//    	User user = registrationService.getUserById(userId);
//    	return Optional.ofNullable(user)
//    	        .map(u -> new ResponseEntity<>("User found" + u.getUsername(), HttpStatus.OK))
//    	        .orElse(new ResponseEntity<>("User not found", HttpStatus.NOT_FOUND));
//
//    }
//
//    @GetMapping("/all")
//    public List<User> getAllUsers() {
//        return registrationService.getAllUsers();
//    }
//}