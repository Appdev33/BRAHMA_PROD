package com.nr.LLD2.bookmyshow.repositories;

import java.util.*;
import java.util.logging.Logger;

import com.nr.LLD2.bookmyshow.interfaces.IRepository;
import com.nr.LLD2.bookmyshow.models.User;
import com.nr.bookmyshow.BookMyShowApp;

public class UserRepository implements IRepository<User, UUID> {
	
	private static final Logger logger = Logger.getLogger(UserRepository.class.getName());
	private Map<UUID,User> userDatabase = new HashMap<>();
	
	@Override
	public Optional<User> add(User entity) {
	    return Optional.ofNullable(entity)
	                   .map(User::getUserId) // Map to Optional<UUID>
	                   .flatMap(userId -> {
	                        userDatabase.put(userId, entity);
	                        return Optional.of(entity);
	                   });
	}

	@Override
	public boolean remove(UUID id) {
		// TODO Auto-generated method stub
		return false;
	}

	
	@Override
	public boolean delete(UUID id) {
		// TODO Auto-generated method stub
		return false;
	}

	@Override
	public Optional<User> getById(UUID id) {
		// TODO Auto-generated method stub
		return Optional.empty();
	}

	@Override
	public boolean update(UUID id, User t) {
		// TODO Auto-generated method stub
		return false;
	}

	

}
