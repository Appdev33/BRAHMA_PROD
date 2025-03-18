package com.nr.LLD2.Spotify.interfaces;

import java.util.ArrayList;
import java.util.Optional;

import com.nr.LLD2.Spotify.models.Track;
import com.nr.LLD2.Spotify.models.User;

//IUserService.java

public interface IRepository<T> {
    T getById(String id);
    ArrayList<T> getAll();
    Optional<ArrayList<T>> getAllOptional();
    void add(T entity);
    void update(T entity);
    void delete(String id);
	void update(String id, T entity);
	ArrayList<String> getKSongs(int count);
}

