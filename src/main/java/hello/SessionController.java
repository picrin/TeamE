package hello;

import hello.beans.AppUser;

import java.util.ArrayList;
import java.util.Calendar;
import java.util.Collections;
import java.util.GregorianCalendar;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.bind.annotation.RequestParam;


@Controller
public class SessionController {
	
	private final long WEEK_IN_MILISECONDS = 1000*60*60*24*7;

	@RequestMapping("/list_session")
	public String session(@RequestParam(value="week", defaultValue="0") String weekStr, Model model) {
		if (!Application.appUser.isInitialized())
			return HomeController.unauthResponse();
		
		int week = Integer.parseInt(weekStr);
		
		ArrayList<Session> sessionsToPrint;
		if (Application.appUser.getUsername().equals(AppUser.TYPE_STUDENT)) {
			sessionsToPrint = Application.adamSessions;
		} else {
			sessionsToPrint = Application.sessions;
		}
		
		model.addAttribute("nextWeek", Integer.toString(week+1));
		model.addAttribute("prevWeek", Integer.toString(week-1));
		model.addAttribute("showPrevWeek", week > 0);
		model.addAttribute("sessionList", filterSessions(sessionsToPrint, week));
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
	public String processAddSession(@ModelAttribute("s") Session s,BindingResult result, Model model) {
		if (!Application.appUser.getType().equals(AppUser.TYPE_TEACHING_ADMIN))
			return HomeController.unauthResponse();
		if(result.hasErrors()){
			return "add_session";
		}

		model.addAttribute("s", s);

		Application.sessions.add(s);

		return "redirect:/list_session";
	}

	@RequestMapping(value = "/add_session")
	public String addSession(Model model) {
		if (!Application.appUser.getType().equals(AppUser.TYPE_TEACHING_ADMIN))
			return HomeController.unauthResponse();
		boolean errorDetected = true;
		Session s = new Session();
		model.addAttribute("s", s);
		model.addAttribute("error", errorDetected);
		return "add_session";
	}

	@ModelAttribute("appUser")
	public AppUser getAppUser() {
		return Application.appUser;
	}

}
