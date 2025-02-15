package com.nr.LLD2.bookmyshow.models;

import java.time.LocalDateTime;
import java.util.UUID;
import java.util.logging.Logger;

public class Payment {
	
	private static final Logger logger = Logger.getLogger(Payment.class.getName());
	
	private UUID paymentID;
	private LocalDateTime timestamp;
	private UUID bookingID;
	private Enum paymentStatus;
	private boolean coupons;
}
