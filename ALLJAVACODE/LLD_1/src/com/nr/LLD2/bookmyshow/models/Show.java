package com.nr.LLD2.bookmyshow.models;

import java.time.LocalDateTime;
import java.util.UUID;
import java.util.logging.Logger;

import com.nr.LLD2.bookmyshow.enums.ShowType;

public class Show {
	
	private static final Logger logger = Logger.getLogger(Show.class.getName());
	
	private Long showId;
	private ShowType showType;
	private String showName;
	private LocalDateTime timestamp;
	private double duration;
	

	public Show(Long showId, ShowType showType, String showName, LocalDateTime timestamp, double duration) {
		this.showId = showId;
		this.showType = showType;
		this.showName = showName;
		this.timestamp = timestamp;
		this.duration = duration;
	}
	
	public Long getShowId() {
		return showId;
	}
	public void setShowId(Long showId) {
		this.showId = showId;
	}
	public ShowType getShowType() {
		return showType;
	}
	public void setShowType(ShowType showType) {
		this.showType = showType;
	}
	public String getShowName() {
		return showName;
	}
	public void setShowName(String showName) {
		this.showName = showName;
	}
	public double getDuration() {
		return duration;
	}
	public void setDuration(double duration) {
		this.duration = duration;
	}

}
