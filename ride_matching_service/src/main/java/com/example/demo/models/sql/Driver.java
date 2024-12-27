package com.example.demo.models.sql;

import java.time.LocalDateTime;
import java.util.Objects;

import com.example.demo.interfaces.SQLModel;
import jakarta.persistence.*;

public class Driver implements SQLModel {


	private final Long id;  // Immutable field
    private String name;
    private String license_number;
    private String vehicle_Id;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;

    // Constructor to ensure proper object creation with validation
    public Driver(Long id, String name, String license_number, LocalDateTime createdAt, LocalDateTime updatedAt) {
        this.id = Objects.requireNonNull(id, "ID cannot be null");
        this.name = Objects.requireNonNull(name, "Name cannot be null");
        this.license_number = Objects.requireNonNull(license_number, "license_number cannot be null");
        this.vehicle_Id = Objects.requireNonNull(vehicle_Id, "vehicle_Id cannot be null");
        this.createdAt = Objects.requireNonNull(createdAt, "Created at cannot be null");
        this.updatedAt = (updatedAt != null) ? updatedAt : createdAt;  // Fallback to createdAt if updatedAt is null
    }

    // Getters and setters
    @Override
    public Long getId() {
        return id;
    }

    @Override
    public void setId(String id) {
        throw new UnsupportedOperationException("ID is immutable and cannot be changed.");
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = Objects.requireNonNull(name, "Name cannot be null");
    }
    
    public String getLicense_number() {
		return license_number;
	}

	public void setLicense_number(String license_number) {
		this.license_number = license_number;
	}

	public String getVehicle_Id() {
		return vehicle_Id;
	}

	public void setVehicle_Id(String vehicle_Id) {
		this.vehicle_Id = vehicle_Id;
	}

    // Implementing timestamp methods from SQLModel
	
    @Override
    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    @Override
    public LocalDateTime getUpdatedAt() {
        return updatedAt;
    }

    @Override
    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = Objects.requireNonNull(createdAt, "Created at cannot be null");
    }

    @Override
    public void setUpdatedAt(LocalDateTime updatedAt) {
        this.updatedAt = (updatedAt != null) ? updatedAt : this.createdAt;  // Fallback to createdAt if null
    }

    // Override toString for better debugging and logging
    @Override
    public String toString() {
        return "Driver{" +
                "id='" + id + '\'' +
                ", name='" + name + '\'' +
                ", email='" + license_number + '\'' +
                ", createdAt=" + createdAt +
                ", updatedAt=" + updatedAt +
                '}';
    }

    // Override equals and hashCode for proper comparison in collections
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Driver driver = (Driver) o;
        return id.equals(driver.id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }
}



