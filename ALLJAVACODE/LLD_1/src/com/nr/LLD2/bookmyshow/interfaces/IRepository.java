package com.nr.LLD2.bookmyshow.interfaces;
import java.util.*;

public interface IRepository<T,ID> {
	Optional<T> add(T entity);
	boolean remove(ID id);
	boolean update(ID id,T entity);
	boolean delete(ID id);
	Optional<T> getById(ID id);
}
