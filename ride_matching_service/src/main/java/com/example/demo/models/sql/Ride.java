package com.example.demo.models.sql;


import java.time.LocalDateTime;

import jakarta.persistence.*;
import lombok.*;

import com.example.demo.enums.RideStatus;
import com.example.demo.interfaces.SQLModel;


import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;
import lombok.Builder;

import java.time.LocalDateTime;

@Getter // Default getters for all fields
@Setter // Default setters for all fields
@NoArgsConstructor
@AllArgsConstructor
@Builder
@ToString
public class Ride implements SQLModel {

    private Long id;

    private String userId;

    private String driverId;

    private Double fare;

    private String pickUpLocation;

    private String dropLocation;

    private RideStatus status;

    private LocalDateTime createdAt;

    @Setter // Restricts only this field's setter
    private LocalDateTime updatedAt;

	@Override
	public Long getId() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public void setId(String id) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public LocalDateTime getCreatedAt() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public LocalDateTime getUpdatedAt() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public void setCreatedAt(LocalDateTime createdAt) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void setUpdatedAt(LocalDateTime updatedAt) {
		// TODO Auto-generated method stub
		
	}
}

