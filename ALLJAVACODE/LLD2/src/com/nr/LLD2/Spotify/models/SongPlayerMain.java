//package com.nr.LLD2.Spotify.models;
//
//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//import java.util.UUID;
//import java.util.*;
//
//public class SongPlayerMain {
//
//	public static void main(String[] args) throws IOException {
//		// TODO Auto-generated method stub
//		
////		UUI uuid;
//
//		Map<String,Album> albums = new HashMap<>();
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		
//		Album a1 = new Album("AC/DC",null);
//		Album a2 = new Album("GreenDay",null);
//		Track t1 = new Track("21Guns",2.09, "metal");
//		Track t2 = new Track("Hell",2.09, "metal");
//		Track t3 = new Track("Some",2.09, "metal");
//		
//		a1.addTrack(t3, "AC/DC");
//		a1.addTrack(t2, "AC/DC");
//		a2.addTrack(t1, "GreenDay");
//		
//		albums.put("AC/DC", a1);
//
//		albums.put("GreenDay", a2);
////		ListIterator<Track> listIterator = a1.listIterator();
//		
//		
//
//		while(true) {
//			
//			
//			
//			
////            "1 - to play next song\n"+
////            "2 - to play previous song\n"+
////            "3 - to replay the current song\n"+
////            "4 - list of all songs \n"+
////            "5 - print all available options\n"+
////            "6 - delete current song");
//			
//			System.out.println("Press \n"
//					+ "1 Create Album \n"
//					+ "2 Add Song To Album \n"
//					+ "3 Delete Song From Album \n"
//					+ "4 Find Song In Album \n"
//					+ "5 Play Song \n"
//					+ "6 Play Next \n"
//					+ "7 Play Previous \n"
////					+ "1 Create Album \n"
////					+ "1 Create Album \n"
////					+ "1 Create Album \n"
////					+ "1 Create Album \n"
//					);
//			System.out.println("Enter choice name/n");
//			int choice = Integer.parseInt(br.readLine());
//			
//			switch(choice){
//				 
//				case 0:{
//					System.exit(0);
//					break;
//				}	
//			
//				case 1: {
//					System.out.println("Enter album name/n");
//					String name = br.readLine();
//					
//					if(albums.containsKey(name)) {
//						System.out.println("Enter new Album Already contains "+name);
//					}
//					albums.put(name,new Album(name,null));
//					System.out.println("New Album Created "+ name + "\n" + albums);
//					
//					break;
//				}
//				
//				
//				case 2: {
//					System.out.println("Enter track name/n");
//					String track = br.readLine();
//					
//					System.out.println("Enter album name/n");
//					String album = br.readLine();
//					
//					System.out.println("Enter track duration/n");
//					double duration = Double.parseDouble(br.readLine());
//					
//					System.out.println("Enter track genre/n");
//					String genre = br.readLine();
//					
//					Track tr=null;
//					List<Track> trks;
//					if(albums.containsKey(album)) {
//						Album  al = albums.get(album);
//						tr = new Track(track, duration, genre);
//						al.addTrack(tr, album);
////						al.getTracks().add(tr);
//						System.out.println("Track added to " + track + "\n" +"Album Created "+ album + "\n" +albums);
//					}else {
//						System.out.println("Current Album "+ album +"not inserted please insert");
//					}
//					
//					break;
//				}
//				
//				case 3: {
//					System.out.println("Enter track name to remove/n");
//					String track = br.readLine();
//					Album album =null;
//					boolean found = false;
//					for (Map.Entry<String,Album> mapElement : albums.entrySet()) {
//				            String key = mapElement.getKey();
//				 
//
//				            album = mapElement.getValue();
////				            for(Track t :album.getTracks()) {
////				            	if(track.equalsIgnoreCase(t.getTrackName())) {
////				            			found =true;
////				            			albums.remove(t);
////				            	}
////				            }
//				            if(found == true)
//		            			break;
//				    }
//				    if(found)
//				    	System.out.println("Track " +track + " removed from album  " + album.getAlbumName() + "\n" +album);
//				    else
//				    	System.out.println("Track Not "+ track +" Found") ; 
//					break;
//				}
//				
//				case 4: {
//					System.out.println("Enter track name/n");
//					String track = br.readLine();
//					Album album =null;
//					boolean found = false;
//					 for (Map.Entry<String,Album> mapElement : albums.entrySet()) {
//				            String key = mapElement.getKey();
//				 
//
//				            album = mapElement.getValue();
//				            for(Track t :album.getTracks()) {
//				            	if(track.equalsIgnoreCase(t.getTrackName())) {
//				            			found =true;
//				            			break;
//				            	}
//				            }
//				            if(found == true)
//		            			break;
//				    }
//				    if(found)
//				    	System.out.println("Track " +track + " found in album  " + album.getAlbumName());
//				    else
//				    	System.out.println("Track Not "+ track +" Found") ; 
//					break;
//				}
//			}
//		}
//	}
//
//}
