package com.example.demo.models.sql;


import java.time.LocalDateTime;
import java.util.Objects;

import jakarta.persistence.*;

import com.example.demo.interfaces.SQLModel;

@Entity
@Table(name = "users")
public class User implements SQLModel {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // Changed to Long to match typical auto-increment database ID behavior

    @Column(nullable = false) // Adds non-null constraint in the database
    private String name;

    @Column(nullable = false, unique = true) // Ensures email is unique and non-null in the database
    private String email;

    @Column(name = "created_at", nullable = false, updatable = false) // Prevent updates to this field
    private LocalDateTime createdAt;

    @Column(name = "updated_at", nullable = false) // Non-null constraint for updatedAt
    private LocalDateTime updatedAt;

    // Default constructor for JPA
    protected User() {
    }

    // Parameterized constructor for manual object creation
    public User(String name, String email) {
        this.name = Objects.requireNonNull(name, "Name cannot be null");
        this.email = Objects.requireNonNull(email, "Email cannot be null");
        this.createdAt = LocalDateTime.now(); // Set default creation time
        this.updatedAt = this.createdAt; // Set default updated time to match createdAt
    }

    // Getters and Setters
    public Long getId() {
        return id;
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
        this.email = Objects.requireNonNull(email, "Email cannot be null");
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public LocalDateTime getUpdatedAt() {
        return updatedAt;
    }

    public void setUpdatedAt(LocalDateTime updatedAt) {
        this.updatedAt = Objects.requireNonNull(updatedAt, "Updated at cannot be null");
    }

    // toString method for debugging and logging
    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", email='" + email + '\'' +
                ", createdAt=" + createdAt +
                ", updatedAt=" + updatedAt +
                '}';
    }

    // equals and hashCode based on ID for entity comparison
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        User user = (User) o;
        return id != null && id.equals(user.id); // Handle cases where ID might be null
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }

	@Override
	public void setId(String id) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void setCreatedAt(LocalDateTime createdAt) {
		// TODO Auto-generated method stub
		
	}
}


