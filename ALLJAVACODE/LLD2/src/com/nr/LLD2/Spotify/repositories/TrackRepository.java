package com.nr.LLD2.Spotify.repositories;

import java.util.ArrayList;
import java.util.Comparator;

//UserRepository.java

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Optional;
import java.util.Set;
import java.util.stream.Collectors;

import com.nr.LLD2.Spotify.interfaces.IRepository;
import com.nr.LLD2.Spotify.interfaces.IUserRepository;
import com.nr.LLD2.Spotify.models.Track;
import com.nr.LLD2.Spotify.models.User;

public class TrackRepository implements IRepository<Track> {
private  Map<String, Track> trackDatabase = new HashMap<>();

private ArrayList<Track> tracks;

@Override
public Track getById(String id) {
	// TODO Auto-generated method stub
	return trackDatabase.get(id);
}

@Override
public ArrayList<Track> getAll() {
	// TODO Auto-generated method stub
	return new ArrayList<>(trackDatabase.values());

}

@Override
public void add(Track track) {
    // TODO Auto-generated method stub
    Optional.ofNullable(track).ifPresentOrElse(
        t -> {
            trackDatabase.put(t.getTrackId(), t);
            System.out.println("Track added successfully: " + t.getTrackId());
        },
        () -> System.out.println("Failed to add track. Input track is null.")
    );
}

@Override
public void update(Track entity) {
	// TODO Auto-generated method stub
    tracks.stream()
    .filter(track -> track.getTrackId().equals(entity.getTrackId())) // Replace with the actual condition
    .findFirst()
    .ifPresent(existingTrack -> {
        // Update the existing track properties
        existingTrack.setTitle(entity.getTitle());
        existingTrack.setArtist(entity.getArtist());
        existingTrack.setDuration(entity.getDuration());
        // Add more properties as needed
    });
}

@Override
public void delete(String id) {
	// TODO Auto-generated method stub
	try {
        // Using Java 8+ Stream API to find and delete the track
        boolean removed = tracks.removeIf(track -> track.getTrackId().equals(id));

        if (removed) {
            System.out.println("Track with ID " + id + " successfully deleted.");
        } else {
            System.out.println("Track with ID " + id + " not found. Deletion failed.");
        }
    } catch (Exception e) {
        System.err.println("An error occurred during track deletion: " + e.getMessage());
    }

}

@Override
public void update(String id, Track entity) {
	// TODO Auto-generated method stub
	
}

@Override
public Optional<ArrayList<Track>> getAllOptional() {
	// TODO Auto-generated method stub
	return Optional.empty();
}

@Override
public ArrayList<String> getKSongs(int count){
	
	System.out.println("helllllll3");	
	ArrayList<String> sortedTracks = trackDatabase.values()
			.stream()
			.sorted(Comparator.comparingInt(Track::getCount).reversed())
			.limit(count)
			.map(track -> track.getTitle() + "--" + track.getDuration() + "--" + track.getCount())
			.collect(Collectors.toCollection(ArrayList::new));
	 
	
	 return sortedTracks;
}

 // Other user-related methods...
}

