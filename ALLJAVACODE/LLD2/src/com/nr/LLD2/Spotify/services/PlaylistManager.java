package com.nr.LLD2.Spotify.services;

import java.util.ArrayList;
import java.util.*;
import java.util.Scanner;

import com.nr.LLD2.Spotify.interfaces.IPlaylistManagerService;
import com.nr.LLD2.Spotify.interfaces.IRepository;
import com.nr.LLD2.Spotify.models.Playlist;
import com.nr.LLD2.Spotify.models.Track;

import java.util.concurrent.atomic.AtomicReference;

public class PlaylistManager implements IPlaylistManagerService{
    private int currentSongIndex;
    private String playlistId;
    private final Object scannerLock = new Object(); // Object for synchronization
    
	private  IRepository playlistRepository;
	private  IRepository trackRepository;

    public PlaylistManager(String playlist, int currentSongIndex,IRepository trackRepository, IRepository playlistRepository) {
		this.currentSongIndex = currentSongIndex;
		this.playlistId = playlist;
		this.playlistRepository = playlistRepository;
		this.trackRepository = trackRepository;
	}

    public void playSongsPlaylist() {
        // Replace this with your actual Playlist and Track classes
        Playlist playlist = (Playlist) playlistRepository.getById(playlistId); // Replace with your actual method or instantiation
        ArrayList<Track> tracks = playlist.getSongs();
        if (tracks.isEmpty()) {
            System.out.println("Playlist is empty");
            return;
        }
        Scanner scanner = new Scanner(System.in);

        AtomicReference<String> userInput = new AtomicReference<>("");

        do {
            Track currentSong = tracks.get(currentSongIndex);
            // Increment the count of the current song using AtomicInteger
            currentSong.incrementCount();	
            System.out.print("Currently playing: " + currentSong.getTitle() + " | ");
            
            System.out.print("Track duration: " + currentSong.getDuration() + " seconds | ");
            System.out.println("Pres n for next : p for previous : r for random : enter key for next");

            Thread userInputThread = new Thread(() -> {
                synchronized (scannerLock) {
                    System.out.print("Elapsed time: ");
                    userInput.set(scanner.nextLine());
                }
            });

            userInputThread.start();

            Thread timerThread = new Thread(() -> {
                int elapsedTime = 0;
                while (!Thread.interrupted() && elapsedTime<currentSong.getDuration()) {
                    try {
                        Thread.sleep(1000);
                        elapsedTime++;
                        System.out.print("\rElapsed time: " + formatTime(elapsedTime) + " | ");
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                    }
                }
            });

            timerThread.start();

            try {
                synchronized (scannerLock) {
                    userInputThread.join((long) (currentSong.getDuration() * 1000));
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            userInputThread.interrupt();
            timerThread.interrupt();

            switch (userInput.get().toLowerCase()) {
                case "n":
                	System.out.println("Playing next song");
                    playNextSong(tracks);
                    break;
                case "p":
                	System.out.println("Playing previous song");
                    playPreviousSong(tracks);
                    break;
                case "r":
                	System.out.println("Playing random song");
                    playRandomSong(tracks);
                    break;
                case "e":
                    // Exit the loop
                    break;
                default:
                    playNextSong(tracks);
            }
        } while (!userInput.get().equalsIgnoreCase("e"));
        System.out.println(); // Move to a new line after exiting the loop
    }


    public String formatTime(int seconds) {
        int minutes = seconds / 60;
        int remainingSeconds = seconds % 60;
        return String.format("%02d:%02d", minutes, remainingSeconds);
    }


	 @Override
	 public void playNextSong(ArrayList<Track> tracks) {
		    currentSongIndex = (currentSongIndex + 1) % tracks.size();
		}
	 
	 public void playPreviousSong(ArrayList<Track> tracks) {
		    currentSongIndex = (currentSongIndex - 1 + tracks.size()) % tracks.size();
		}

	@Override
	public void playRandomSong(ArrayList<Track> tracks) {
		 int randomIndex = (int) (Math.random() * tracks.size());
	        currentSongIndex = randomIndex;
	}
}

