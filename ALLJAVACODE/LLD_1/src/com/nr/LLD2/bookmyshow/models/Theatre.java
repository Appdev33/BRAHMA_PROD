package com.nr.LLD2.bookmyshow.models;

import java.time.LocalDateTime;
import java.util.UUID;
import java.util.logging.Logger;

public class Theatre {
	
	private static final Logger logger = Logger.getLogger(Theatre.class.getName());
	
	private int theatreID;
	private String Location;
	private int seatsCount;
	private UUID bookingID;
	
}
