package com.nr.LLD2.Spotify.interfaces;

import java.util.ArrayList;

import com.nr.LLD2.Spotify.models.Track;
import com.nr.LLD2.Spotify.models.User;

//IUserRepository.java

public interface ITrackService {
 void add(Track track);
 void update(String trackId, Track updatedTrack);
 Track get(String trackId);
 // Other user-related methods...
 ArrayList<Track> getAllTracks();
ArrayList<String> getKSongs(int count);
}

