package com.nr.LLD2.bookmyshow.models;

import java.time.LocalDateTime;
import java.util.UUID;
import java.util.logging.Logger;

public class Seat {
	
	private static final Logger logger = Logger.getLogger(Seat.class.getName());
	
	private String seatID;
	private double price;
	private Enum status;
	private UUID bookingID;
	
}
