package hello;

import hello.beans.AppUser;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class HomeController {
	
	@Autowired
	AppUser appUser = new AppUser();
	
	@RequestMapping("/")
    public String index(Model model) {
		if (appUser.isInitialized()) {
			return "home/home";
		} else {
			return "redirect:/signin";
		}
    }
	
	@RequestMapping(value = "/signin", method = RequestMethod.GET)
	public String login(Model model) {
		return "home/signin";
	}
	
	@RequestMapping(value = "/signin", method = RequestMethod.POST)
	@ResponseBody
	public String login(@RequestParam(value="guid") String guid,
			@RequestParam(value="password") String password, Model model) {
		
		AppUser newUser = null;
		if (guid.equals("admin")) {
			newUser = new AppUser();
			newUser.setUsername(guid);
			newUser.setType(AppUser.TYPE_TEACHING_ADMIN);
		} else if (guid.equals("student")) {
			newUser = new AppUser();
			newUser.setUsername(guid);
			newUser.setType(AppUser.TYPE_STUDENT);
		}
		
		if (newUser != null) {
			appUser = newUser;
			return "{\"success\": 1}";
		} else {
			return "{\"success\": 0}";
		}
	}
	
	@RequestMapping(value = "/signout")
	public String signout(Model model) {
		appUser = new AppUser();
		return "redirect:/signin";
	}
	
	@ModelAttribute("appUser")
    public AppUser getAppUser() {
        return appUser;
    }
}
