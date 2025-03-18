package com.nr.LLD2.Spotify.models;

import java.util.ArrayList;
import java.util.List;

public class User {
	
	private String userId;
    private String username;
    private String email;
    private ArrayList<Playlist> playlists;
    
    
    public User() {
		// TODO Auto-generated constructor stub
	}
    
    public User(String userId, String username, String email) {
        this.userId = userId;
        this.username = username;
        this.email = email;
        this.playlists = new ArrayList<>();
    }

	public ArrayList<Playlist> getPlaylists() {
        return playlists;
    }

    public void setPlaylists(ArrayList<Playlist> playlists) {
        this.playlists = playlists;
    }

    public void addPlaylist(Playlist playlist) {
        if (playlists == null) {
            playlists = new ArrayList<>();
        }
        playlists.add(playlist);
    }

    public void removePlaylist(Playlist playlist) {
        playlists.remove(playlist);
    }
    
    
    public String getUserId() {
		return userId;
	}
	public void setUserId(String userId) {
		this.userId = userId;
	}
	public String getUsername() {
		return username;
	}
	public void setUsername(String username) {
		this.username = username;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}

	@Override
	public String toString() {
		return "User [userId=" + userId + ", username=" + username + ", email=" + email + ", playlists=" + playlists
				+ ", getPlaylists()=" + getPlaylists() + ", getUserId()=" + getUserId() + ", getUsername()="
				+ getUsername() + ", getEmail()=" + getEmail() + "]";
	}

	
}
