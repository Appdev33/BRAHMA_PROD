package com.nr.LLD2.bookmyshow.repositories;

import java.util.HashMap;
import java.util.Map;
import java.util.Optional;
import java.util.logging.Logger;

import com.nr.LLD2.bookmyshow.interfaces.IRepository;
import com.nr.LLD2.bookmyshow.models.Show;
import java.util.concurrent.ConcurrentHashMap;

public class ShowRepository implements IRepository<Show, Long> {
	
	private static final Logger logger = Logger.getLogger(UserRepository.class.getName());
	private Map<Long, Show> showDatabase = new ConcurrentHashMap<>();

	@Override
	public Optional<Show> add(Show entity) {
		if(entity==null)
			return Optional.empty();
		else 
			return Optional.ofNullable(entity)
	                   .map(Show::getShowId) // Map to Optional<UUID>
	                   .flatMap(showId -> {
	                	   showDatabase.put(showId, entity);
	                        return Optional.of(entity);
	                   });
	}

	public boolean remove(Long id) {
        return showDatabase.remove(id) != null;
    }


    public boolean delete(Long id) {
        return remove(id);
    }

    public Optional<Show> getById(Long id) {
        return Optional.ofNullable(showDatabase.get(id));
    }

	@Override
	public boolean update(Long id, Show updatedShow) {
		if (showDatabase.containsKey(id)) {
            showDatabase.put(id, updatedShow);
            return true;
        }
        return false;
	}

}
