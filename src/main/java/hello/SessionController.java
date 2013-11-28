package hello;

import java.util.ArrayList;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
public class SessionController {

	@RequestMapping("/list_session")
	public String session(Model model) {
		ArrayList<String> sessionStrings = new ArrayList<String>(2);
		sessionStrings.add("while");
		sessionStrings.add("not");
		model.addAttribute("sessionList", sessionStrings);
		model.addAttribute("mySession", sessionStrings.get(0));
		return "list_session";
	}

	@RequestMapping(value = "/session_added", method = RequestMethod.POST)
	public String processAddSession(@ModelAttribute(value = "date") Session s,
			Model model) {

		model.addAttribute("s", s);
		System.out.println(s.getDate());
		return "session_added";
	}

	@RequestMapping(value = "/add_session")
	public String addSession(Model model) {
		Session s = new Session();
		model.addAttribute("s", s);
		return "add_session";
	}

}
