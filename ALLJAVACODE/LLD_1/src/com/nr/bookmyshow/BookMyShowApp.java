package com.nr.bookmyshow;

import com.nr.LLD2.bookmyshow.interfaces.*;
import com.nr.LLD2.bookmyshow.services.*;

import java.util.logging.Logger;

import com.nr.LLD2.bookmyshow.controllers.*;
import com.nr.LLD2.bookmyshow.repositories.*;

public class BookMyShowApp {

	private static final Logger logger = Logger.getLogger(BookMyShowApp.class.getName());

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		logger.info("Intialising Book My show App : " );
		
		IRepository userRepository = new UserRepository();

        IUserService userService = new UserService(userRepository);
        // Initialize controller
        UserController userController = new UserController(userService);
        
        userController.addUser("Karan", "Hypervisor");
        
		IRepository showRepository = new ShowRepository();

        IShowService showService = new ShowService(showRepository);
        // Initialize controller
        ShowController showController = new ShowController(showService);
        showController.addShow(null, null, null, 0);
        
        logger.info("Intialising Book My show Apps : " );

	}

}
