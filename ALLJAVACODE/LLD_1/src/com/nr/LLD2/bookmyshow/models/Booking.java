package com.nr.LLD2.bookmyshow.models;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.UUID;
import java.util.logging.Logger;

public class Booking {
	
	private static final Logger logger = Logger.getLogger(Booking.class.getName());

	
	private UUID bookingID;
	private LocalDateTime timestamp;
	private int seatsCount;
	private User userID;
	private Show showID;
//	private Payment paymentID;
//	private Notification notificationID;
	
	
	 // Log user creation
//    logger.info("User created: " + username + ", ID: " + userId);
	
}
