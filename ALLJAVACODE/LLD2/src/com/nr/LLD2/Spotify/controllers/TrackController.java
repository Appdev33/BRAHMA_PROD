package com.nr.LLD2.Spotify.controllers;

import java.util.ArrayList;

import com.nr.LLD2.Spotify.interfaces.ITrackService;
import com.nr.LLD2.Spotify.interfaces.IUserService;
import com.nr.LLD2.Spotify.models.Track;
import com.nr.LLD2.Spotify.models.User;

//UserController.java

public class TrackController {
 
private ITrackService trackService;

 public TrackController(ITrackService trackService) {
     this.trackService = trackService;
 }

 // Example endpoint methods
 public void createTrack(Track track) {
	 trackService.add(track);
 }

 public void updateUser(String trackId, Track updatedTrack) {
	 trackService.update(trackId, updatedTrack);
 }

 public Track getTrack(String trackId) {
     return trackService.get(trackId);
 }
 
  public ArrayList<Track> getAllTracks(){
	  return trackService.getAllTracks();
  }
  
  public ArrayList<String> getTopKSongs(int count){
	   return trackService.getKSongs(count);
  }
}

