package hello;

import hello.beans.AppUser;

import java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.context.annotation.ComponentScan;

@ComponentScan
@EnableAutoConfiguration
public class Application {
	
	@Autowired
	public static AppUser appUser = new AppUser();
	
	public static ArrayList<Session> sessions = new ArrayList<>();
	public static ArrayList<Session> adamSessions = new ArrayList<>();
	public static ArrayList<Session> ivaSessions = new ArrayList<>();
	public static ArrayList<Session> brunoSessions = new ArrayList<>();

	
	public static void main(String[] args) {
		SpringApplication.run(Application.class, args);
	}

}
