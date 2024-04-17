package com.brahma.microservices;

import org.springframework.boot.SpringApplication;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class UserOnboardingServiceApplication {
	
	private static final Logger logger = LoggerFactory.getLogger(UserOnboardingServiceApplication.class);


	public static void main(String[] args) {
		
		SpringApplication.run(UserOnboardingServiceApplication.class, args);
		logger.info("#################Received request on /example endpoint##########");
	}

}
