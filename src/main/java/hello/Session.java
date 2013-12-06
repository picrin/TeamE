package hello;

import java.util.Date;

import org.springframework.format.annotation.DateTimeFormat;

public class Session {
	
	/**
	 * The date of the first session
	 */
	@DateTimeFormat(pattern = "dd/MM/yyyy")
	private Date date;
	@DateTimeFormat(pattern = "hh:mm")
	private Date time;
	@DateTimeFormat(pattern = "hh:mm")
	private Date duration;
	/**
	 * Number of weeks between every session
	 */
	private int repeatFrequency;
	
	private String lecturer;
	private int maxAttendance;
	private String compulsory;
	private String venue;

	public Session(Date date, Date time, Date duration, int repeatFrequency,
			String lecturer, int maxAttendance, String compulsory, String venue) {
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

	public Date getTime() {
		return time;
	}

	public void setTime(Date time) {
		this.time = time;
	}

	public Date getDuration() {
		return duration;
	}

	public void setDuration(Date duration) {
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
