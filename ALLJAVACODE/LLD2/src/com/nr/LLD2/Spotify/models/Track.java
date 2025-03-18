package com.nr.LLD2.Spotify.models;
import java.util.concurrent.atomic.AtomicInteger;

public class Track {
	
//	private int songID;
//	private String albumID;
	private String trackId;
	private String title;
    private String artist;
    private double duration;
    private AtomicInteger count; // Using AtomicInteger for thread safety
    private int index;
    
    
    public Track() {
		// TODO Auto-generated constructor stub
    	count = new AtomicInteger(0);
	}
    
    
    public String getTrackId() {
		return trackId;
	}
	public void setTrackId(String trackId) {
		this.trackId = trackId;
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getArtist() {
		return artist;
	}
	public void setArtist(String artist) {
		this.artist = artist;
	}
	public double getDuration() {
		return duration;
	}
	public void setDuration(double duration) {
		this.duration = duration;
	}
	
	public int getCount() {
        return count.get();
    }

    public void setCount(int count) {
        this.count.set(count);
    }

    public void incrementCount() {
        count.incrementAndGet();
    }


	public int getIndex() {
		return index;
	}
	public void setIndex(int index) {
		this.index = index;
	}

}


