package com.nr.LLD2.Spotify;

import com.nr.LLD2.Spotify.models.User;
import com.nr.LLD2.Spotify.models.Playlist;
import com.nr.LLD2.Spotify.models.Track;
import com.nr.LLD2.Spotify.repositories.*;

import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Optional;
import java.io.BufferedReader;
import java.io.IOException;

import com.nr.LLD2.Spotify.controllers.UserController;
import com.nr.LLD2.Spotify.interfaces.IUserService;
import com.nr.LLD2.Spotify.interfaces.IRepository;
import com.nr.LLD2.Spotify.interfaces.IUserRepository;
import com.nr.LLD2.Spotify.interfaces.*;
import com.nr.LLD2.Spotify.repositories.TrackRepository;
import com.nr.LLD2.Spotify.services.*;
import com.nr.LLD2.Spotify.controllers.*;

public class App {

    public static void main(String[] args) throws  IOException {
        // Initialize repository
        IUserRepository userRepository = new UserRepository();

        // Initialize service
        IUserService userService = new UserService(userRepository);

        // Initialize controller
        UserController userController = new UserController(userService);
        
        
        IRepository trackRepo = new TrackRepository();
        ITrackService trackService = new TrackService(trackRepo);
        TrackController trackController = new TrackController(trackService);
        
        
        IRepository playlistRepo = new PlaylistRepository();
        IPlaylistService playlistService = new PlaylistService(playlistRepo);
        PlaylistController playlistController = new PlaylistController(playlistService);
        
        IPlaylistManagerService playlistManager;
       
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // Create a sample user
        User user1 =  new User();
        user1.setUserId("12");
        user1.setUsername("karan");
        user1.setEmail("karan@gmail.com");
        User user2 =  new User();
        user2.setUserId("13");
        user2.setUsername("Amit");
        user2.setEmail("Amit@gmail.com");
        User user3 =  new User();
        user3.setUserId("14");
        user3.setUsername("Prakash");
        user3.setEmail("prakash@gmail.com");
        userController.createUser(user1);
        userController.createUser(user2);
        userController.createUser(user3);
        
        Track track1 = new Track();
        track1.setArtist("Linkin Park");
        track1.setTitle(" Leave out all the rest");
        track1.setTrackId("1");
        track1.setDuration(3.01);
        
        Track track2 = new Track();
        track2.setArtist("Led Zepplin");
        track2.setTitle(" Stairway to Heaven");
        track2.setTrackId("2");
        track2.setDuration(3.6);
        
        Track track3 = new Track();
        track3.setArtist("Lana Del Ray");
        track3.setTitle(" Summer Time Sadness");
        track3.setTrackId("3");
        track3.setDuration(4.20);
        
        Track track4 = new Track();
        track4.setArtist("Green Day");
        track4.setTitle(" Twenty one Guns");
        track4.setTrackId("4");
        track4.setDuration(4.20);
        
        Track track5 = new Track();
        track5.setArtist("Eagles");
        track5.setTitle("Hotel California");
        track5.setTrackId("5");
        track5.setDuration(4.20);
        
        trackController.createTrack(track1);
        trackController.createTrack(track2);
        trackController.createTrack(track3);
        trackController.createTrack(track4);
        trackController.createTrack(track5);
        
        playlistController.createPlaylist("1", "Personal");
        playlistController.createPlaylist("2", "Common");
        playlistController.createPlaylist("3", "Private");
        
        System.out.println("******************");

        System.out.println(user2.toString());

        
        userController.addPlaylist(user1.getUserId(), playlistController.getPlaylist("1") );
        userController.addPlaylist(user2.getUserId(), playlistController.getPlaylist("2"));
        userController.addPlaylist(user2.getUserId(), playlistController.getPlaylist("3"));
        
        playlistController.addSongToPlaylist("3", track1);
        playlistController.addSongToPlaylist("3", track2);
        playlistController.addSongToPlaylist("3", track3);
        playlistController.addSongToPlaylist("3", track4);
        playlistController.addSongToPlaylist("3", track5);
        
        
        while(true) {
			
			System.out.println("\n\nPress \n"
					+ "1 Create User \n"
					+ "2 Find User \n"
					+ "3 Display all Users \n"
					+ "4 Create Track \n"
					+ "5 Create playlist \n"
					+ "6 Display All tracks \n"
					+ "7 Create Playlist  \n"
					+ "8 Add song to Playlist  \n"
					+ "9 Shuffle playlist \n"
					+ "10 Enter into Playing Mode  \n"
					+ "11 List top K Songs Played  \n"
					+ "12 To exit player  \n"
					);
			System.out.println("Enter choice name/n");
			int choice = Integer.parseInt(br.readLine());
			
			switch(choice){
						case 0:{
							System.exit(0);
							break;
						}	
						case 1: {
							
							System.out.println("Enter userId of user");
					        String id = br.readLine();
					        System.out.println("Enter name of user");
					        String name = br.readLine();
					        System.out.println("Enter email of user");
					        String email = br.readLine();
					        
					        User newUser = new User();
					        newUser.setUserId(id);
					        newUser.setUsername(name);
					        newUser.setEmail(email);
					
					        // Use the controller to create the user
					        userController.createUser(newUser);
					        System.out.println("Successful user details");
					        break;	
						}
						case 2: {
					        System.out.println("Enter userId of user");
					        String id = br.readLine();
					        
					        Optional<User> retrievedUser = Optional.ofNullable(userController.getUser(id));
					        retrievedUser.ifPresentOrElse(
					                user -> System.out.println("User Retrieved: " + user.getUsername()),
					                () -> System.out.println("User not found.")
					        );
					        break;
						}
						case 3: {
							ArrayList<User> users = userController.getAllUsers();
							users.stream().forEach(u->
									{		
									System.out.print(u.getUsername());
									System.out.print(" "+u.getEmail());
									System.out.print(" "+u.getUserId());
									System.out.println();
									}
									);
							break;
						}
						case 4: {
							System.out.println("Enter trackId of track");
					        String trackId = br.readLine();
					        System.out.println("Enter title of track");
					        String title = br.readLine();
					        System.out.println("Enter artist of track");
					        String artist = br.readLine();
					        System.out.println("Enter duration of track");
					        double duration = Double.parseDouble(br.readLine());
					        
					        Track newTrack = new Track();
					        newTrack.setArtist(artist);
					        newTrack.setTitle(title);
					        newTrack.setTrackId(trackId);
					        newTrack.setDuration(duration);
					
					        // Use the controller to create the user
					        trackController.createTrack(newTrack);
					        System.out.println("Successful track created details" + newTrack.toString() );
					        break;	
						}
						case 5: {
					        System.out.println("Enter playlistId of track");
					        String playlistId = br.readLine();
					        System.out.println("Enter playlistId name");
					        String playlistName = br.readLine();
					        System.out.println("Enter userId name");
					        String userId = br.readLine();
					        userController.addPlaylist(userId, playlistController.getPlaylist(playlistId));
					        boolean playlistadd = 	playlistController.createPlaylist(playlistId, playlistName);
					        if(playlistadd) {
					        	System.out.println("Successfully added new Playlist");
					        }else {
						        	System.out.println("Error adding new Playlist");
					        }
					        break;
						}
						case 6: {
							ArrayList<Track> tracks = trackController.getAllTracks();
							tracks.stream().forEach(u->
									{		
									System.out.print(u.getTitle());
									System.out.print(" "+u.getArtist());
									System.out.print(" "+u.getDuration());
									System.out.println();
									}
									);
							break;
						}
						case 7: {
					        System.out.println("Enter playlistId of track");
					        String playlistId = br.readLine();
					        System.out.println("Enter playlistId name");
					        String playlistName = br.readLine();
							playlistController.createPlaylist(playlistId, playlistName);
							break;
						}
						case 8: {
							playlistController.printAllPlaylist();
					        System.out.println("Enter playlistId of playlist");
					        String playlistId = br.readLine();
					        System.out.println("Enter trackId name");
					        String trackId = br.readLine();
//					        System.out.println("Enter userId ");
					        
					        playlistController.addSongToPlaylist(playlistId, trackController.getTrack(trackId));
					        playlistController.printAllPlaylist();
					        playlistController.printPlaylistSongs(playlistId);
//							userController.getAllUsersPlaylist(userController.getUser(userId).getUserId());
							break;
						}
						case 9: {
					        System.out.println("Enter playlistId to Shuffle");
					        String playlistId = br.readLine();
					        System.out.println("Current Playlist Songs:");
					        playlistController.printPlaylistSongs(playlistId);
					        System.out.println("Songs after Playlist shuffle:");
					        ArrayList<Track> tracks = playlistController.getPlaylist(playlistId).getSongs();
					        Collections.shuffle(tracks);
					        playlistController.printPlaylistSongs(playlistId);
							break;
						}
						case 10:{
					        System.out.println("Enter playlistId of playlist");
					        String playlistId = br.readLine();
							playlistManager = new PlaylistManager(playlistId, 0, trackRepo, playlistRepo);
							playlistManager.playSongsPlaylist();
							break;
						}
						case 11:{
							System.out.println("Enter value of K top K songs list");
							int count = Integer.parseInt(br.readLine());
							if(trackRepo.getAll().size()<count ) {
								System.out.println("Size k is too large...");
								System.out.println("Current Size"+trackRepo.getAll().size());
							}else {
								System.out.println(trackController.getTopKSongs(count));
							}
							break;
						}
						default: {
							System.out.println("Enter a valid choice from options");
						}
			}
        }
    }
}

