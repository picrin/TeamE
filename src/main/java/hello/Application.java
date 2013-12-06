package hello;

import hello.beans.AppUser;

import java.util.ArrayList;
import java.util.Date;

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
		Date date1 = new Date(2013, 10, 7); //1st of October, monday PSD3 morning session
		Date time1 = new Date(0, 0, 0, 9, 0, 0); //
		Date duration1 = new Date(0, 0, 0, 1, 30, 0);
		int repeatFrequency = 0;
		String jeremy = "Jeremy Singer";
		int maxAttendance = 10;
		String compulsory = "mandatory";
		String venue = "Boyd Orr";

		Session adamSession1 = new Session(date1, time1, duration1, repeatFrequency, jeremy, maxAttendance, compulsory, venue);
		adamSessions.add(adamSession1);
		SpringApplication.run(Application.class, args);
	}

}
