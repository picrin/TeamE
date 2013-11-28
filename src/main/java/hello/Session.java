package hello;

import java.sql.Time;
import java.util.Date;

public class Session {

	private Date date;
	private Time time;
	private long duration;
	private int repeatFrequency;
	private String lecturer;
	private int maxAttendance;
	private String compulsory;
	private String venue;

	public Session(Date date, Time time, long duration, int repeatFrequency,
			String lecturer, int maxAttendance, String compulsory, String venue) {
		super();
		this.date = date;
		this.time = time;
		this.duration = duration;
		this.repeatFrequency = repeatFrequency;
		this.lecturer = lecturer;
		this.maxAttendance = maxAttendance;
		this.compulsory = compulsory;
		this.venue = venue;
	}

	public Session() {
	
	}

	public Date getDate() {
		return date;
	}

	public void setDate(Date date) {
		this.date = date;
	}

	public Time getTime() {
		return time;
	}

	public void setTime(Time time) {
		this.time = time;
	}

	public long getDuration() {
		return duration;
	}

	public void setDuration(long duration) {
		this.duration = duration;
	}

	public int getRepeatFrequency() {
		return repeatFrequency;
	}

	public void setRepeatFrequency(int repeatFrequency) {
		this.repeatFrequency = repeatFrequency;
	}

	public String getLecturer() {
		return lecturer;
	}

	public void setLecturer(String lecturer) {
		this.lecturer = lecturer;
	}

	public int getMaxAttendance() {
		return maxAttendance;
	}

	public void setMaxAttendance(int maxAttendance) {
		this.maxAttendance = maxAttendance;
	}

	public String getCompulsory() {
		return compulsory;
	}

	public void setCompulsory(String compulsory) {
		this.compulsory = compulsory;
	}

	public String getVenue() {
		return venue;
	}

	public void setVenue(String venue) {
		this.venue = venue;
	}

}
