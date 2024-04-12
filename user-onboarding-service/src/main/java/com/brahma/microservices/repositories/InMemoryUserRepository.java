package com.brahma.microservices.repositories;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Repository;

import com.brahma.microservices.interfaces.IUserRepository;
import com.brahma.microservices.model.User;

@Repository
public class InMemoryUserRepository implements IUserRepository {
    private final Map<Long, User> userMap = new HashMap<>();
    private static long idCounter = 1;

    @Override
    public void save(User user) {
        if (user.getId() == null) {
            user.setId(idCounter++);
        }
        userMap.put(user.getId(), user);
    }

    @Override
    public User findById(Long id) {
        return userMap.get(id);
    }

    @Override
    public List<User> findAll() {
        return new ArrayList<>(userMap.values());
    }
}
