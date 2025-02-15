package com.nr.LLD2.Spotify.interfaces;

import java.util.ArrayList;

import com.nr.LLD2.Spotify.models.Track;

public interface IPlaylistManagerService {
	void playNextSong(ArrayList<Track> tracks);
	void playPreviousSong(ArrayList<Track> tracks);
	void playRandomSong(ArrayList<Track> tracks);
	void playSongsPlaylist();
	
}
