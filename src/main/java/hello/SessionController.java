package hello;

import hello.beans.AppUser;

import java.util.ArrayList;
import java.util.Calendar;
import java.util.Collections;
import java.util.GregorianCalendar;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class SessionController {
	
	private final long WEEK_IN_MILISECONDS = 1000*60*60*24*7;

	@RequestMapping("/list_session")
	public String session(@RequestParam(value="week", defaultValue="0") String week, Model model) {
		if (!Application.appUser.isInitialized())
			return HomeController.unauthResponse();
		
		ArrayList<Session> sessionsToPrint;
		if (Application.appUser.getUsername().equals(AppUser.TYPE_STUDENT)) {
			sessionsToPrint = Application.adamSessions;
		} else {
			sessionsToPrint = Application.sessions;
		}
		
		model.addAttribute("week", week);
		model.addAttribute("sessionList", filterSessions(sessionsToPrint, Integer.parseInt(week)));
		return "list_session";
	}
	
	private ArrayList<Session> filterSessions(ArrayList<Session> allSessions, int week) {
		ArrayList<Session> result = new ArrayList<Session>();
		if (allSessions.size() == 0)
			return result;
		
		Collections.sort(allSessions);
		
		Calendar mondayZero = new GregorianCalendar();
		mondayZero.setTime(allSessions.get(0).getDate());
		mondayZero.set(Calendar.DAY_OF_WEEK, Calendar.MONDAY);
		
		for (Session session: allSessions) {
			long startWeek = (session.getDate().getTime() - mondayZero.getTime().getTime()) / WEEK_IN_MILISECONDS;
			if (week >= startWeek && ((week - startWeek) % session.getRepeatFrequency() == 0)) {
				result.add(session);
			}
		}
		return result;
	}

	@RequestMapping(value = "/session_added", method = RequestMethod.POST)
	public String processAddSession(@ModelAttribute("s") Session s, Model model) {
		if (!Application.appUser.getType().equals(AppUser.TYPE_TEACHING_ADMIN))
			return HomeController.unauthResponse();

		model.addAttribute("s", s);

		Application.sessions.add(s);

		return "redirect:/list_session";
	}

	@RequestMapping(value = "/add_session")
	public String addSession(Model model) {
		if (!Application.appUser.getType().equals(AppUser.TYPE_TEACHING_ADMIN))
			return HomeController.unauthResponse();

		Session s = new Session();
		model.addAttribute("s", s);
		return "add_session";
	}

	@ModelAttribute("appUser")
	public AppUser getAppUser() {
		return Application.appUser;
	}

}
