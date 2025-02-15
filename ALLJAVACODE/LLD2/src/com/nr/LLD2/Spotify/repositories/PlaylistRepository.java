package com.nr.LLD2.Spotify.repositories;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;

import com.nr.LLD2.Spotify.interfaces.IRepository;
import com.nr.LLD2.Spotify.models.Playlist;
import com.nr.LLD2.Spotify.models.Track;

public class PlaylistRepository implements IRepository<Playlist>{
	private Map<String, Playlist> playlistDatabase = new HashMap<>();
	
	private ArrayList<Playlist> playlist;

	@Override
	public Playlist getById(String id) {
		// TODO Auto-generated method stub
		return playlistDatabase.get(id);
	}

	 @Override
    public ArrayList<Playlist> getAll() {
        if (playlistDatabase != null) {
            return new ArrayList<>(playlistDatabase.values());
        } else {
            // You may choose to handle the case where playlistDatabase is null.
            // For now, returning an empty ArrayList.
            return new ArrayList<>();
        }
    }
	
	@Override
    public Optional<ArrayList<Playlist>> getAllOptional() {
        return Optional.ofNullable(playlistDatabase)
                .map(db -> new ArrayList<>(db.values().stream().collect(Collectors.toList())));
    }

	@Override
	public void add(Playlist playlist) {
		// TODO Auto-generated method stub
		Optional.ofNullable(playlist).ifPresentOrElse(
		        t -> {
		        	playlistDatabase.put(t.getId(), t);
		            System.out.println("Track added successfully: " + t.getId());
		        },
		        () -> System.out.println("Failed to add track. Input track is null.")
		    );
	}

	@Override
	public void update(Playlist entity) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void delete(String id) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void update(String id, Playlist entity) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public ArrayList<String> getKSongs(int count) {
		// TODO Auto-generated method stub
		return null;
	}

}
