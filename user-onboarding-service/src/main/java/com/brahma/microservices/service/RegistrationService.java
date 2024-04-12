package com.brahma.microservices.service;



import java.util.List;
import java.util.Optional;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
//import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.brahma.microservices.interfaces.IUserRepository;
import com.brahma.microservices.model.User;


//@Service
//public class RegistrationService {
//
//    private final IUserRepository userRepository;
//
//    @Autowired
//    public RegistrationService(IUserRepository userRepository) {
//        this.userRepository = userRepository;
//    }
//
//    public void registerNewUser(User user) {
//        // Perform registration logic
//
//        // Save the user to the database
//        userRepository.save(user);
//    }
//
//    public User findUserByUsername(String username) {
//        // Retrieve a user by their username
//        return userRepository.findByUsername(username).orElse(null);
//    }
//
//	public Optional<User> findUserById(Long id) {
//		// TODO Auto-generated method stub
//		return userRepository.findById(id);
//	}
//
//    // Add more methods based on your registration service logic
//
//}

@Service
public class RegistrationService {
    private final IUserRepository userRepository;
    
    
    @Autowired
    public RegistrationService(IUserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public void onboardUser(String username, String password) {
        User newUser = new User();
        newUser.setUsername(username);
        newUser.setPassword(password);

        userRepository.save(newUser);
    }
    
//    @RolesAllowed("admin")
    public User getUserById(Long userId) {
        return userRepository.findById(userId);
    }

    public List<User> getAllUsers() {
        return userRepository.findAll();
    }
}
