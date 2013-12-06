package hello;

import hello.beans.AppUser;

import java.util.ArrayList;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;


@Controller
public class SessionController {

	@RequestMapping("/list_session")
	public String session(Model model) {
		ArrayList<Session> sessionToPrint;
		if (Application.appUser.getUsername().equals(AppUser.TYPE_STUDENT)) {
			sessionToPrint = Application.adamSessions;
		} else {
			sessionToPrint = Application.sessions;
		}
		model.addAttribute("sessionList", sessionToPrint);
		return "list_session";
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
