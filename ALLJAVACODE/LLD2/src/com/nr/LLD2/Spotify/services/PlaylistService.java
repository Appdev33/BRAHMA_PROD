package com.nr.LLD2.Spotify.services;

import java.util.ArrayList;
import java.util.Optional;

import com.nr.LLD2.Spotify.interfaces.IPlaylistService;
import com.nr.LLD2.Spotify.interfaces.IRepository;
import com.nr.LLD2.Spotify.models.Playlist;
import com.nr.LLD2.Spotify.models.Track;
import com.nr.LLD2.Spotify.models.User;

public class PlaylistService implements IPlaylistService{
	

	 private final IRepository playlistRepository;

	 public PlaylistService(IRepository playlistRepository) {
	     this.playlistRepository = playlistRepository;
	 }
	
//	private IRepository playlistRepository;
//	
//	
//	 public PlaylistService(IPlaylistRepository playlistRepository) {
//	     this.playlistRepository = playlistRepository;
//	 }

	 @Override
	 public boolean createPlaylist(Playlist playlist) {
	     try {
	         playlistRepository.add(playlist);
	         System.out.println("Playlist "+ playlist.getName() + "created");
	         return true; // Return true if addition is successful
	     } catch (Exception e) {
	    	 System.out.println("Playlist "+ playlist.getName() + "creation issue");
	         e.printStackTrace(); // Handle the exception according to your application's requirements
	         return false; // Return false if an exception occurs
	     }
	 }
	 
	 @Override
	 public boolean addSongToPlaylist(String playlistId, Track song) {
	        try {
//	        	
//	        	Optional<Playlist> optionalPlaylist = ((Optional<Playlist>) playlistRepository.getById(playlistId))
//	                    .map(result -> (result instanceof Playlist) ? (Playlist) result : null);

	        	boolean optionalPlaylist = playlistRepository.getById(playlistId) != null;
	            if (optionalPlaylist) {
	                Playlist playlist = (Playlist)playlistRepository.getById(playlistId);

	                // Ensure that the playlist's songs list is initialized
	                if (playlist.getSongs() == null) {
	                    playlist.setSongs(new ArrayList<>());
	                }

	                // Add the song to the playlist
	                playlist.getSongs().add(song);

	                // Update the playlist in the repository
	                playlistRepository.update(playlist);

	                return true; // Return true if addition is successful
	            } else {
	                System.out.println("Playlist with ID " + playlistId + " not found.");
	                return false; // Return false if the playlist is not found
	            }
	        } catch (Exception e) {
	            e.printStackTrace(); // Log or handle the exception according to your application's requirements
	            return false; // Return false if an exception occurs
	        }
	    } 
	 
	@Override
	public void updatePlaylist(String playlistId, Playlist updatedPlaylist) {
		// TODO Auto-generated method stub
		playlistRepository.update(playlistId, updatedPlaylist);
	}

	@Override
	public Playlist getPlaylist(String playlistId) {
		// TODO Auto-generated method stub
		return (Playlist)playlistRepository.getById(playlistId);
	}

	@Override
	public void getAllPlaylist() {
		// TODO Auto-generated method stub
		
		ArrayList<Playlist> playlists = playlistRepository.getAll();
		if(playlists!=null) {
		playlists.stream().forEach(p-> {
			System.out.print(p.getName() + " ");
			System.out.println(p.getId());
		});
		}
		System.out.println();
	}

	@Override
	public void getSongsAllSongs(String playlistId) {
		// TODO Auto-generated method stub
		Playlist playlist = (Playlist) playlistRepository.getById(playlistId);
		System.out.println(playlist.getName());
		playlist.getSongs().stream().forEach(p->{
			System.out.println(p.getTitle());
		});
	}
}
