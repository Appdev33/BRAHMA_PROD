package com.example.demo.services;

import java.util.List;

import com.example.demo.dto.UserRequestDTO;
import com.example.demo.dto.UserResponseDTO;

public interface IUserService {
	
    UserResponseDTO createUser(UserRequestDTO userRequestDTO);
    UserResponseDTO getUserById(Long id);
    List<UserResponseDTO> getAllUsers();
	UserResponseDTO updateUser(Long id, UserRequestDTO userRequestDTO);
	boolean deleteUser(Long id);
    
}
