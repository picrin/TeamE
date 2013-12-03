package hello;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
public class SessionController {

	@RequestMapping("/list_session")
	public String session(Model model) {

		model.addAttribute("sessionList", Application.sessions);

		return "list_session";
	}

	@RequestMapping(value = "/session_added", method = RequestMethod.POST)
	public String processAddSession(@ModelAttribute("s") Session s, Model model) {

		model.addAttribute("s", s);

		Application.sessions.add(s);

		return "list_session";
	}

	@RequestMapping(value = "/add_session")
	public String addSession(Model model) {
		Session s = new Session();
		model.addAttribute("s", s);
		return "add_session";
	}

}
