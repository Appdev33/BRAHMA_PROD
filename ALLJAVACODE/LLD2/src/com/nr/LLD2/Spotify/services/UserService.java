package com.nr.LLD2.Spotify.services;

import java.util.ArrayList;

import com.nr.LLD2.Spotify.interfaces.IUserRepository;
import com.nr.LLD2.Spotify.interfaces.IUserService;
import com.nr.LLD2.Spotify.models.Playlist;
import com.nr.LLD2.Spotify.models.User;
import com.nr.LLD2.Spotify.repositories.UserRepository;

//UserService.java

public class UserService implements IUserService {
 

 private final IUserRepository userRepository;

 public UserService(IUserRepository userRepository) {
     this.userRepository = userRepository;
 }

 @Override
 public void createUser(User user) {
     // Additional logic, validation, etc. can be added here.
	 
	 userRepository.add(user);
 }

 @Override
 public void updateUser(String userId, User updatedUser) {
     // Additional logic, validation, etc. can be added here.
     userRepository.update(userId, updatedUser);
 }

 @Override
 public User getUser(String userId) {
     // Additional logic, validation, etc. can be added here.
     return userRepository.get(userId);
 }

@Override
public ArrayList<User> getAllUsers() {
	// TODO Auto-generated method stub
	return userRepository.getAll();
}


@Override
public boolean addPlaylistToUser(String userId, Playlist playlistToAdd) {
	// TODO Auto-generated method stub
	User user = userRepository.get(userId);
	ArrayList<Playlist> userPlaylists = user.getPlaylists();
	
	if(userPlaylists!=null && user!=null) {
		userPlaylists.add(playlistToAdd);
		return true;
	}
	else
		return false;
}

@Override
public void getAllUsersPlaylist(String userId) {
		ArrayList<Playlist> playlists =  userRepository.getPlaylist(userId);
	}
}

