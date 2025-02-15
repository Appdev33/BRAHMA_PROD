package com.nr.LLD2.Spotify.interfaces;

import java.util.ArrayList;

import com.nr.LLD2.Spotify.models.Playlist;
import com.nr.LLD2.Spotify.models.User;

//IUserRepository.java

public interface IUserRepository {
 void add(User user);
 void update(String userId, User updatedUser);
 User get(String userId);
 ArrayList<User> getAll();
 ArrayList<Playlist> getPlaylist(String playlistId);

 
}

