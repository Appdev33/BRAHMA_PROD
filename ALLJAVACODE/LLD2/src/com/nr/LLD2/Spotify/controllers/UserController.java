package com.nr.LLD2.Spotify.controllers;

import java.util.ArrayList;

import com.nr.LLD2.Spotify.interfaces.IUserService;
import com.nr.LLD2.Spotify.models.Playlist;
import com.nr.LLD2.Spotify.models.User;

//UserController.java

public class UserController {
 
private IUserService userService;

 public UserController(IUserService userService) {
     this.userService = userService;
 }

 // Example endpoint methods
 public void createUser(User user) {
     userService.createUser(user);
 }

 public void updateUser(String userId, User updatedUser) {
     userService.updateUser(userId, updatedUser);
 }

 public User getUser(String userId) {
     return userService.getUser(userId);
 }
 
 public ArrayList<User> getAllUsers(){
	 return userService.getAllUsers();
 }
 
 public void getAllUsersPlaylist(String userId){
	 userService.getAllUsersPlaylist(userId);
 }
 
 
 public boolean addPlaylist(String userId, Playlist playlistToAdd){
	return userService.addPlaylistToUser(userId, playlistToAdd);
 }

}

