package com.nr.LLD2.bookmyshow.controllers;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.UUID;

import com.nr.LLD2.bookmyshow.enums.ShowType;
import com.nr.LLD2.bookmyshow.interfaces.IShowService;
import com.nr.LLD2.bookmyshow.interfaces.IUserService;
import com.nr.LLD2.bookmyshow.models.Booking;

public class ShowController {

	private IShowService showService;

	 public ShowController(IShowService showService) {
	     this.showService = showService;
	 }
	 
	private Long showId;
	private ShowType showType;
	private String showName;
	private LocalDateTime timestamp;
	private double duration;
	
	public boolean addShow(String showId, ShowType showType, String showName, double duration ) {
		return showService.addShow(showId, showName, showType, duration) != null;
	 }
}
