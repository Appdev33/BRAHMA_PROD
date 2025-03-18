package com.nr.LLD2.Spotify.controllers;

import java.util.ArrayList;

import com.nr.LLD2.Spotify.interfaces.IPlaylistService;
import com.nr.LLD2.Spotify.interfaces.ITrackService;
import com.nr.LLD2.Spotify.models.Playlist;
import com.nr.LLD2.Spotify.models.Track;

public class PlaylistController {
	
	private IPlaylistService playlistService;
	
	
	 public PlaylistController(IPlaylistService playlistService) {
	     this.playlistService = playlistService;
	 }
	
    public boolean createPlaylist(String playlistId, String playlistName) {
        try {
            Playlist newPlaylist = new Playlist();
            newPlaylist.setId(playlistId);
            newPlaylist.setName(playlistName);
            newPlaylist.setSongs(new ArrayList<>());

            // Delegate to the repository for persistence
            return playlistService.createPlaylist(newPlaylist);
        } catch (Exception e) {
            e.printStackTrace(); // Handle the exception according to your application's requirements
            return false;
        }
    }
    
    public Playlist getPlaylist(String id) {
    	return playlistService.getPlaylist(id);
    }
     
	public void addSongToPlaylist(String playlistId, Track song) {
		   // Delegate to the service for adding a song to the playlist
        playlistService.addSongToPlaylist(playlistId, song);
	}
	
	public void printPlaylistSongs(String playlistId) {
		playlistService.getSongsAllSongs(playlistId);
	}
	
	public boolean shufflePlaylist(String playlistId) {
		return false;
	}


	public void printAllPlaylist() {
		// TODO Auto-generated method stub
		playlistService.getAllPlaylist();
	} 
}
