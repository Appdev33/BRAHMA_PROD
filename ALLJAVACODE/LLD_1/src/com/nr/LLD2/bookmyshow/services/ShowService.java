package com.nr.LLD2.bookmyshow.services;

import java.util.Optional;

import com.nr.LLD2.bookmyshow.enums.ShowType;
import com.nr.LLD2.bookmyshow.interfaces.IRepository;
import com.nr.LLD2.bookmyshow.interfaces.IShowService;

public class ShowService<Show> implements IShowService {
	
	private final IRepository showRepository;

	 public ShowService(IRepository showRepository) {
	     this.showRepository = showRepository;
	 }
	 
	@Override
	public Optional<Show> addShow(String showId, String showName, ShowType showType, double duration) {
		
		
		return null;
	}

	@Override
	public boolean removeShow() {
		// TODO Auto-generated method stub
		return false;
	}

	@Override
	public boolean updateShow() {
		// TODO Auto-generated method stub
		return false;
	}

	@Override
	public boolean deleteShow() {
		// TODO Auto-generated method stub
		return false;
	}

}
