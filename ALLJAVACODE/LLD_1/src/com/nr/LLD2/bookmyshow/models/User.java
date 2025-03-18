package com.nr.LLD2.bookmyshow.models;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.UUID;
import java.util.logging.Logger;

public class User {

	private static final Logger logger = Logger.getLogger(User.class.getName());
	
	private String username;
	private String password;
	private UUID userId;
	private LocalDateTime timestamp;
	private ArrayList<Booking> bookings;
	
	
	
	public User(String username, String password, UUID userId, LocalDateTime timestamp) {
		this.username = username;
		this.password = password;
		this.userId = userId;
		this.timestamp = timestamp;
		
		logger.info("User object created with username: " + username +" "+ password +" " + userId +" "+ timestamp);
	}



	public String getUsername() {
		return username;
	}
	
	public void setUsername(String username) {
		this.username = username;
	}
	
	public String getPassword() {
		return password;
	}
	
	public void setPassword(String password) {
		this.password = password;
	}
	
	public UUID getUserId() {
		return userId;
	}
	
	public void setUserId(UUID userId) {
		this.userId = userId;
	}
	
	public LocalDateTime getTimestamp() {
		return timestamp;
	}
	
	public void setTimestamp(LocalDateTime timestamp) {
		this.timestamp = timestamp;
	}
	
	public ArrayList<Booking> getBookings() {
		return bookings;
	}
	
	public void setBookings(ArrayList<Booking> bookings) {
		this.bookings = bookings;
	}
	
	public static Logger getLogger() {
		return logger;
	}

}
