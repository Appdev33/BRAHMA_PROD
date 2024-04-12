package com.brahma.microservices.interfaces;

import com.brahma.microservices.model.User;

//public interface IUserRepository extends JpaRepository<User, Long> {
//    Optional<User> findByUsername(String username);
//
//    // Add more custom queries as needed based on your requirements
//}
import java.util.List;
import java.util.Map;

import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Repository;


@Repository
public interface IUserRepository {
    void save(User user);
    User findById(Long id);
    List<User> findAll();
}



//public interface IUserRepository extends JpaRepository<User, Long> {
//
//
//
//}