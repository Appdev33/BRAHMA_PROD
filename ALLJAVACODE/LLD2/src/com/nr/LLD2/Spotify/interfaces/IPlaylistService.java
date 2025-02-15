package com.nr.LLD2.Spotify.interfaces;

import com.nr.LLD2.Spotify.models.Playlist;
import com.nr.LLD2.Spotify.models.Track;

//IUserService.java

public interface IPlaylistService {
// void createPlaylist(Playlist playlist);
 boolean createPlaylist(Playlist playlist);
 void updatePlaylist(String playlistId, Playlist updatedPlaylist);
 Playlist getPlaylist(String playlistId);
 
 boolean addSongToPlaylist(String id,Track song);
 // Other user-related methods...
void getAllPlaylist();
void getSongsAllSongs(String playlistId);
}

