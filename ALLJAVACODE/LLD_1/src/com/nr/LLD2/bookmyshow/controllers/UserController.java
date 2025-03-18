package com.nr.LLD2.bookmyshow.controllers;

import java.security.MessageDigest;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Optional;
import java.util.UUID;

import com.nr.LLD2.bookmyshow.interfaces.IUserService;
import com.nr.LLD2.bookmyshow.models.Booking;
import com.nr.LLD2.bookmyshow.models.User;

public class UserController {
	
	private IUserService userService;

	 public UserController(IUserService userService) {
	     this.userService = userService;
	 }
	 
	private String username;
	private String password;
	private UUID userId;
	private LocalDateTime timestamp;
	private ArrayList<Booking> bookings;
	
	public boolean addUser(String username, String password) {
		return userService.addUser(username, password) != null;
	 }
	 
	 
}
