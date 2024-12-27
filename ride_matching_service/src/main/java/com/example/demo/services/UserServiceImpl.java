package com.example.demo.services;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

import com.example.demo.dto.UserRequestDTO;
import com.example.demo.dto.UserResponseDTO;
import com.example.demo.exceptions.DatabaseException;
import com.example.demo.exceptions.ResourceNotFoundException;
import com.example.demo.models.sql.User;
import com.example.demo.repostitories.UserRepository;

import java.time.LocalDateTime;
import java.util.List;
import java.util.UUID;
import java.util.concurrent.CompletableFuture;
import java.util.stream.Collectors;

@Service
public class UserServiceImpl implements IUserService {

    private final UserRepository userRepository;

    @Autowired
    public UserServiceImpl(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Override
    public UserResponseDTO createUser(UserRequestDTO userRequestDTO) {
        User user = new User(
                userRequestDTO.getName(),
                userRequestDTO.getEmail()

        );
        User savedUser = userRepository.save(user);
        return mapToResponseDTO(savedUser);
    }

    @Override
    public UserResponseDTO getUserById(Long id) {
        User user = userRepository.findById(id).orElseThrow(() -> new ResourceNotFoundException("User not found with ID: " + id));
        return mapToResponseDTO(user);
    }

    @Override
    public List<UserResponseDTO> getAllUsers() {
        List<User> users = userRepository.findAll();
        return users.stream()
                .map(this::mapToResponseDTO)
                .collect(Collectors.toList());
    }

    @Override
    public UserResponseDTO updateUser(Long id, UserRequestDTO userRequestDTO) {
        User existingUser = userRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("User not found with ID: " + id));

        existingUser.setName(userRequestDTO.getName());
        existingUser.setEmail(userRequestDTO.getEmail());
        existingUser.setUpdatedAt(LocalDateTime.now());

        User updatedUser = userRepository.save(existingUser);
        return mapToResponseDTO(updatedUser);
    }

    @Override
    public boolean deleteUser(Long id) {

        try {
            // Attempt to find the user by ID
            User existingUser = userRepository.findById(id)
                    .orElseThrow(() -> new ResourceNotFoundException("User not found with ID: " + id));

            // Attempt to delete the user
            userRepository.delete(existingUser);
//            logger.info("User with ID {} successfully deleted.", id); // Log successful deletion

            return true;  // Return true indicating successful deletion
        } catch (ResourceNotFoundException e) {
//            logger.error("Error deleting user: {}", e.getMessage());  // Log the exception message for resource not found
            throw e;  // Rethrow the custom exception to inform the caller
        } catch (Exception e) {
            // Catch other unforeseen errors
//            logger.error("Unexpected error while deleting user with ID {}: {}", id, e.getMessage());
            throw new DatabaseException("An unexpected error occurred while deleting the user."); // Custom database exception
        }
    }


    // Utility method to map User entity to UserResponseDTO
    private UserResponseDTO mapToResponseDTO(User user) {
        return new UserResponseDTO(
        		user.getId(),
        		user.getName(),
        		user.getEmail(),
        		user.getCreatedAt()
        		);
    }
}
//@Service
//public class UserServiceImpl implements IUserService {
//
//    @Autowired
//    private UserRepository userRepository;
//
//    // Asynchronously create user
//    @Override
//    @Async
//    public CompletableFuture<UserResponseDTO> createUser(UserRequestDTO userRequestDTO) {
//        User user = new User(userRequestDTO.getName(), userRequestDTO.getEmail());
//        User savedUser = userRepository.save(user);
//        return CompletableFuture.completedFuture(new UserResponseDTO(savedUser));
//    }
//
//    // Asynchronously get user by ID
//    @Override
//    @Async
//    public CompletableFuture<UserResponseDTO> getUserById(String id) {
//        Optional<User> user = userRepository.findById(id);
//        return CompletableFuture.completedFuture(user.map(UserResponseDTO::new).orElse(null));
//    }
//
//    // Asynchronously get all users
//    @Override
//    @Async
//    public CompletableFuture<List<UserResponseDTO>> getAllUsers() {
//        List<User> users = userRepository.findAll();
//        return CompletableFuture.completedFuture(users.stream().map(UserResponseDTO::new).toList());
//    }
//
//    // Asynchronously update user
//    @Override
//    @Async
//    public CompletableFuture<UserResponseDTO> updateUser(String id, UserRequestDTO userRequestDTO) {
//        Optional<User> existingUser = userRepository.findById(id);
//        if (existingUser.isPresent()) {
//            User user = existingUser.get();
//            user.setName(userRequestDTO.getName());
//            user.setEmail(userRequestDTO.getEmail());
//            User updatedUser = userRepository.save(user);
//            return CompletableFuture.completedFuture(new UserResponseDTO(updatedUser));
//        }
//        return CompletableFuture.completedFuture(null);
//    }
//
//    // Asynchronously delete user
//    @Override
//    @Async
//    public CompletableFuture<Boolean> deleteUser(String id) {
//        Optional<User> user = userRepository.findById(id);
//        if (user.isPresent()) {
//            userRepository.delete(user.get());
//            return CompletableFuture.completedFuture(true);
//        }
//        return CompletableFuture.completedFuture(false);
//    }
//}





