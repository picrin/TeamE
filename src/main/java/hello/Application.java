package hello;

import hello.beans.AppUser;

import java.util.ArrayList;
import java.util.Date;
import java.util.Random;

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
		
		generateMockData();
		
		SpringApplication.run(Application.class, args);
	}
	
	private static void generateMockData(){
		
		final int MOCK_ENTRIES = 30;
		Random rand = new Random();
		String[] compulsoryOptions = {"Mandatory", "Optional"}; 
		
		for (int i = 0; i < MOCK_ENTRIES; i++) {
			
			int randomDay = rand(0,29);
			int randomMonth = rand(0,11);
			int randomHour = rand(8,18);
			
			Date date1 = new Date(113, randomMonth, randomDay); // Starting at random Month and Day
			Date time1 = new Date(0, 0, 0, randomHour, 0, 0); // Starting at random Hour
			Date duration1 = new Date(0, 0, 0, 1, 30, 0); // 1h30 long
			
			int randomRepeatFreq = rand.nextInt((11 - 0) + 1);
			
			String jeremy = "Jeremy Singer";
			int maxAttendance = rand(40,120);
			String compulsory = compulsoryOptions[rand.nextInt(compulsoryOptions.length)];;
			String venue = "Boyd Orr";
			Session adamSession1 = new Session(date1, time1, duration1, randomRepeatFreq, jeremy, maxAttendance, compulsory, venue);
			
			adamSessions.add(adamSession1);
		}
		
		ivaSessions = (ArrayList<Session>) adamSessions.clone();
		brunoSessions = (ArrayList<Session>) adamSessions.clone();
		sessions = (ArrayList<Session>) adamSessions.clone();
		
	}
	
	public static int rand(int min, int max) {

	    Random rand = new Random();

	    int randomNum = rand.nextInt((max - min) + 1) + min;

	    return randomNum;
	}

}
