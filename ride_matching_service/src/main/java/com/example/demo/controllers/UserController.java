package com.example.demo.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.dto.UserRequestDTO;
import com.example.demo.dto.UserResponseDTO;
import com.example.demo.exceptions.ResourceNotFoundException;
import com.example.demo.services.IUserService;

import jakarta.validation.Valid;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@RestController
@RequestMapping("/api/users")
public class UserController {
	
	private static final Logger logger = LoggerFactory.getLogger(UserController.class);

    @Autowired
    private IUserService userService;

    @PostMapping
    public ResponseEntity<UserResponseDTO> createUser(@Valid @RequestBody UserRequestDTO userRequestDTO) {
        logger.info("Creating user with username: {}", userRequestDTO.getName());
        UserResponseDTO response = userService.createUser(userRequestDTO);
        logger.info("User created successfully with ID: {}", response.getId());
        return ResponseEntity.ok(response);
    }

    @GetMapping("/{id}")
    public ResponseEntity<UserResponseDTO> getUserById(@PathVariable Long id) {
        logger.debug("Fetching user with ID: {}", id);
        UserResponseDTO response = userService.getUserById(id);
        logger.debug("User fetched successfully: {}", response);
        return ResponseEntity.ok(response);
    }

    @PatchMapping("/{id}")
    public ResponseEntity<UserResponseDTO> updateUser(@PathVariable Long id, @Valid @RequestBody UserRequestDTO userRequestDTO) {
        logger.info("Updating user with ID: {}", id);
        UserResponseDTO response = userService.updateUser(id, userRequestDTO);
        logger.info("User updated successfully: {}", response);
        return ResponseEntity.ok(response);
    }

    @GetMapping
    public ResponseEntity<List<UserResponseDTO>> getAllUsers()  {
        logger.info("Fetching all users");
        List<UserResponseDTO> users = userService.getAllUsers();
        logger.info("Successfully fetched all users, count: {}", users.size());
        return ResponseEntity.ok(users);
    }


    
    @DeleteMapping("/{id}")
    public ResponseEntity<String> deleteUser(@PathVariable Long id) {
        try {
            boolean isDeleted = userService.deleteUser(id);  // Attempt to delete the user

            if (isDeleted) {
                logger.info("User with ID {} successfully deleted.", id);  // Log successful deletion
                return ResponseEntity
                        .status(HttpStatus.NO_CONTENT)  // 204 No Content
                        .body("User with ID " + id + " deleted successfully.");  // Message body
            } else {
                logger.warn("User with ID {} not found for deletion.", id);  // Log when user is not found
                return ResponseEntity
                        .status(HttpStatus.NOT_FOUND)  // 404 Not Found
                        .body("User with ID " + id + " not found for deletion.");  // Message body
            }
        } catch (ResourceNotFoundException e) {
            logger.error("User deletion failed: {}", e.getMessage());  // Log error with exception message
            return ResponseEntity
                    .status(HttpStatus.NOT_FOUND)  // 404 Not Found
                    .body("Error: " + e.getMessage());  // Message body with exception details
        } catch (Exception e) {
            logger.error("Unexpected error occurred while deleting user with ID {}: {}", id, e.getMessage());  // Log unexpected error
            return ResponseEntity
                    .status(HttpStatus.INTERNAL_SERVER_ERROR)  // 500 Internal Server Error
                    .body("Unexpected error occurred while deleting the user: " + e.getMessage());  // Message body
        }
    }   
}



//@RestController
//@RequestMapping("/api/users")
//public class UserController {
//
//    @Autowired
//    private IUserService userService;
//
//    // Create user asynchronously
//    @PostMapping
//    public CompletableFuture<ResponseEntity<UserResponseDTO>> createUser(@Valid @RequestBody UserRequestDTO userRequestDTO) {
//        return userService.createUser(userRequestDTO)
//                          .thenApply(user -> ResponseEntity.status(HttpStatus.CREATED).body(user));
//    }
//
//    // Get user by ID asynchronously
//    @GetMapping("/{id}")
//    public CompletableFuture<ResponseEntity<UserResponseDTO>> getUserById(@PathVariable String id) {
//        return userService.getUserById(id)
//                          .thenApply(user -> user != null ? ResponseEntity.ok(user) : ResponseEntity.notFound().build());
//    }
//
//    // Get all users asynchronously
//    @GetMapping
//    public CompletableFuture<ResponseEntity<List<UserResponseDTO>>> getAllUsers() {
//        return userService.getAllUsers()
//                          .thenApply(users -> ResponseEntity.ok(users));
//    }
//
//    // Update user asynchronously
//    @PutMapping("/{id}")
//    public CompletableFuture<ResponseEntity<UserResponseDTO>> updateUser(@PathVariable String id, @Valid @RequestBody UserRequestDTO userRequestDTO) {
//        return userService.updateUser(id, userRequestDTO)
//                          .thenApply(user -> user != null ? ResponseEntity.ok(user) : ResponseEntity.notFound().build());
//    }
//
//    // Delete user asynchronously
//    @DeleteMapping("/{id}")
//    public CompletableFuture<ResponseEntity<Void>> deleteUser(@PathVariable String id) {
//        return userService.deleteUser(id)
//                          .thenApply(result -> result ? ResponseEntity.noContent().build() : ResponseEntity.notFound().build());
//    }
//}
