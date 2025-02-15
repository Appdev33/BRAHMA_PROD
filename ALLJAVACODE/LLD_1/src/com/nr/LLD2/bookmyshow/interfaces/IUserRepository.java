package com.nr.LLD2.bookmyshow.interfaces;

import com.nr.LLD2.bookmyshow.models.User;

public interface IUserRepository {
	
	boolean add();
	boolean remove();
	boolean update();
	User get();
}
