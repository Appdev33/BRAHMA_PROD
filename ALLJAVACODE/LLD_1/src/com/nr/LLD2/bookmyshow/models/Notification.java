package com.nr.LLD2.bookmyshow.models;

import java.time.LocalDateTime;
import java.util.UUID;
import java.util.logging.Logger;

public class Notification {
	
	private static final Logger logger = Logger.getLogger(Notification.class.getName());
	
	private UUID notificationID;
	private LocalDateTime timestamp;
	private String notificationType;
	
}
