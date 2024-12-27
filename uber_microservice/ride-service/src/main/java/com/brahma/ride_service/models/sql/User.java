package com.brahma.ride_service.models.sql;

import java.time.LocalDateTime;
import java.util.Objects;
import com.brahma.ride_service.interfaces.SQLModel;
import javax.persistence.*;

public class User implements SQLModel {

    private final String id;  // Immutable field
    private String name;
    private String email;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;

    // Constructor to ensure proper object creation with validation
    public User(String id, String name, String email, LocalDateTime createdAt, LocalDateTime updatedAt) {
        this.id = Objects.requireNonNull(id, "ID cannot be null");
        this.name = Objects.requireNonNull(name, "Name cannot be null");
        this.email = Objects.requireNonNull(email, "Email cannot be null");
        this.createdAt = Objects.requireNonNull(createdAt, "Created at cannot be null");
        this.updatedAt = (updatedAt != null) ? updatedAt : createdAt;  // Fallback to createdAt if updatedAt is null
    }

    // Getters and setters
    @Override
    public String getId() {
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

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        // Simple validation, can be enhanced with regex for email format validation
        Objects.requireNonNull(email, "Email cannot be null");
        this.email = email;
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
        return "User{" +
                "id='" + id + '\'' +
                ", name='" + name + '\'' +
                ", email='" + email + '\'' +
                ", createdAt=" + createdAt +
                ", updatedAt=" + updatedAt +
                '}';
    }

    // Override equals and hashCode for proper comparison in collections
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        User user = (User) o;
        return id.equals(user.id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }
}
