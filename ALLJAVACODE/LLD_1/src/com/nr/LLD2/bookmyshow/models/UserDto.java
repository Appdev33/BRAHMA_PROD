package com.nr.LLD2.bookmyshow.models;

import java.time.LocalDateTime;
import java.util.UUID;

public class UserDto {
	private String username;
	private String password;
	private UUID userId;
	private LocalDateTime timestamp;
	
	public UserDto(String username, String password, UUID userId, LocalDateTime timestamp) {
		this.username = username;
		this.password = password;
		this.userId = userId;
		this.timestamp = timestamp;
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
	
	
	
	
}
