package com.nr.LLD2.Spotify.repositories;

import java.util.ArrayList;

//UserRepository.java

import java.util.HashMap;
import java.util.Map;

import com.nr.LLD2.Spotify.interfaces.IUserRepository;
import com.nr.LLD2.Spotify.models.Playlist;
import com.nr.LLD2.Spotify.models.User;

public class UserRepository implements IUserRepository {
 private Map<String, User> userDatabase = new HashMap<>();

 @Override
 public void add(User user) {
     // Additional logic, validation, etc. can be added here.
     userDatabase.put(user.getUserId(), user);
 }

 @Override
 public void update(String userId, User updatedUser) {
     // Additional logic, validation, etc. can be added here.
     userDatabase.put(userId, updatedUser);
 }

 @Override
 public User get(String userId) {
     // Additional logic, validation, etc. can be added here.
     return userDatabase.get(userId);
 }

@Override
public ArrayList<User> getAll() {
	// TODO Auto-generated method stub
	return new ArrayList<>(userDatabase.values());
}

@Override
public ArrayList<Playlist> getPlaylist(String userId) {
	// TODO Auto-generated method stub
	return userDatabase.get(userId).getPlaylists();
}



 // Other user-related methods...
}

