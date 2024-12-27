package com.brahma.ride_service.interfaces;

import java.time.LocalDateTime;

public interface SQLModel extends BaseModel{
	
	LocalDateTime getCreatedAt();
	LocalDateTime getUpdatedAt();
	
    void setCreatedAt(LocalDateTime createdAt);
    void setUpdatedAt(LocalDateTime updatedAt);
}
