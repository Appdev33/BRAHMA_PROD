package com.nr.LLD2.Spotify.models;

import java.util.ArrayList;
import java.util.List;

public class Playlist {
	
	private String id;
	private String name;
	private ArrayList<Track> songs;

	
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public ArrayList<Track> getSongs() {
		return songs;
	}
	public void setSongs(ArrayList<Track> songs) {
		this.songs = songs;
	}
	@Override
	public String toString() {
		return "Playlist [id=" + id + ", name=" + name + ", songs=" + songs + ", getId()=" + getId() + ", getName()="
				+ getName() + ", getSongs()=" + getSongs() + "]";
	}
	
}
