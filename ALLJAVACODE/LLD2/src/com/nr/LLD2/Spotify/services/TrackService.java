package com.nr.LLD2.Spotify.services;

import java.util.ArrayList;

import com.nr.LLD2.Spotify.interfaces.IRepository;
import com.nr.LLD2.Spotify.interfaces.ITrackService;
import com.nr.LLD2.Spotify.interfaces.IUserRepository;
import com.nr.LLD2.Spotify.interfaces.IUserService;
import com.nr.LLD2.Spotify.models.Track;
import com.nr.LLD2.Spotify.models.User;
import com.nr.LLD2.Spotify.repositories.UserRepository;

//UserService.java

public class TrackService implements ITrackService {
 

 private final IRepository trackRepository;

 public TrackService(IRepository trackRepository) {
     this.trackRepository = trackRepository;
 }

	@Override
	public void add(Track track) {
		// TODO Auto-generated method stub
		trackRepository.add(track);
	}
	
	@Override
	public Track get(String trackId) {
		// TODO Auto-generated method stub
		return (Track) trackRepository.getById(trackId);
	}

	@Override
	public void update(String trackId, Track updatedTrack) {
		// TODO Auto-generated method stub
		trackRepository.update(trackId,updatedTrack);
	}

	@Override
	public ArrayList<Track> getAllTracks() {
		// TODO Auto-generated method stub
		return trackRepository.getAll();
	}
	
	public ArrayList<String> getKSongs(int count) {

		return ( trackRepository).getKSongs(count);  // bad practice use composition or extend interface behaviour
	}
	 // Other user-related methods...
}

