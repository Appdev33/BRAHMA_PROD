package com.nr.LLD2.bookmyshow.interfaces;

import java.util.Optional;

public interface IUserService<T> {
	Optional<T> addUser(String use, String pass);
    boolean removeUser();
    boolean updateUser();
    boolean deleteUser();
    
}
