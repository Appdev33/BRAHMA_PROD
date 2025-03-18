package com.nr.LLD2.bookmyshow.services;


import java.security.MessageDigest;
import java.time.LocalDateTime;
import java.util.Optional;
import java.util.UUID;

import com.nr.LLD2.bookmyshow.exceptions.NoSuchAlgorithmException;
import com.nr.LLD2.bookmyshow.interfaces.IRepository;
import com.nr.LLD2.bookmyshow.interfaces.IUserService;
import com.nr.LLD2.bookmyshow.models.User;

public class UserService implements IUserService{

	private final IRepository userRepository;

	 public UserService(IRepository userRepository) {
	     this.userRepository = userRepository;
	 }
	 
	@Override
	public Optional<User> addUser(String username, String password) {
		 try {
	            // Generate unique user ID
	            UUID userId = UUID.randomUUID();
	            // Encrypt the password securely
	            String hashedPassword = null;
				try {
					hashedPassword = hashPassword(password);
				} catch (java.security.NoSuchAlgorithmException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
	            // Create User object
				User user = new User(username, hashedPassword, userId, LocalDateTime.now());
	            // Store the user in the repository
	            return userRepository.add(user);
	        } catch (NoSuchAlgorithmException e) {
	            // Handle hashing algorithm exception
	            e.printStackTrace();
	            return Optional.empty();
	        }
	 }
	 
	 private String hashPassword(String password) throws NoSuchAlgorithmException, java.security.NoSuchAlgorithmException {
	        MessageDigest md = MessageDigest.getInstance("SHA-256");
	        md.update(password.getBytes());
	        byte[] hashBytes = md.digest();
	        StringBuilder sb = new StringBuilder();
	        for (byte b : hashBytes) {
	            sb.append(String.format("%02x", b));
	        }
	        return sb.toString();
	    }

	@Override
	public boolean removeUser() {
		// TODO Auto-generated method stub
		return false;
	}

	@Override
	public boolean updateUser() {
		// TODO Auto-generated method stub
		return false;
	}

	@Override
	public boolean deleteUser() {
		// TODO Auto-generated method stub
		return false;
	}

}
