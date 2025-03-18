package com.nr.LLD2.bookmyshow.interfaces;

import java.util.Optional;

import com.nr.LLD2.bookmyshow.enums.ShowType;

public interface IShowService<T> {
    boolean removeShow();
    boolean updateShow();
    boolean deleteShow();
	Optional<T> addShow(String showId, String showName, ShowType showType, double duration);
}