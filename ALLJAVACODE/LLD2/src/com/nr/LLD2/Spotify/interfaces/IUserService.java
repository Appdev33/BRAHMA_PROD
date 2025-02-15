package com.nr.LLD2.Spotify.interfaces;

import java.util.ArrayList;

import com.nr.LLD2.Spotify.models.Playlist;
import com.nr.LLD2.Spotify.models.User;

//IUserService.java

public interface IUserService {
 void createUser(User user);
 void updateUser(String userId, User updatedUser);
 User getUser(String userId);
 ArrayList<User> getAllUsers();	
 // Other user-related methods...
 boolean addPlaylistToUser(String userId, Playlist playlistToAdd);
 void getAllUsersPlaylist(String userId);

}

