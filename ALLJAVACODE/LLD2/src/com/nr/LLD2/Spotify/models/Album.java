package com.nr.LLD2.Spotify.models;

import java.util.*;

public class Album {
//	String album_ID;
	private String albumName;
//	String releaseDate;
	private List<Track> tracks;
	
	
	
	
	public Album(String albumName, List<Track> tracks) {
//		super();
		this.albumName = albumName;
		this.tracks = tracks;
	}
	
	
	public boolean addTrack(Track track, String albumName) {
		
		if(tracks==null || tracks.isEmpty()) {
			tracks = new LinkedList<>();
		}
		
		tracks.add(track);
		
		return true;
	}
	
	public boolean findTrack(Track track,  String albumName) {
		
		for(Track t : tracks) {
			if(track.equals(t))
				return true;
		}
		
		return false;
	}
	
	public boolean deleteTrack(Track track,  String albumName) {
		boolean foundTrack = false;
		
		for(Track t : tracks) {
			if(track.equals(t)) 
				tracks.remove(t);
				foundTrack = true;
		}
		
		return (foundTrack==true)?true:false;
		
	}
	
	
	public String getAlbumName() {
		return albumName;
	}
	public void setAlbumName(String albumName) {
		this.albumName = albumName;
	}
	public List<Track> getTracks() {
		return tracks;
	}
	public void setTracks(List<Track> tracks) {
		this.tracks = tracks;
	}
	
	@Override
	public String toString() {
		return "Album [albumName=" + albumName + ", tracks=" + tracks + "]";
	}
	
	
	
	
}
