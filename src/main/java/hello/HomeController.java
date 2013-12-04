package hello;

import hello.beans.AppUser;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class HomeController {
	
	@RequestMapping("/")
    public String index(Model model) {
		if (Application.appUser.isInitialized()) {
			return "home/home";
		} else {
			return unauthResponse();
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
			Application.appUser = newUser;
			return "{\"success\": 1}";
		} else {
			return "{\"success\": 0}";
		}
	}
	
	@RequestMapping(value = "/signout")
	public String signout(Model model) {
		Application.appUser = new AppUser();
		return unauthResponse();
	}
	
	/**
	 * To disallow unsigned or unauthorized users to visit links
	 * put this at the top of http response methods:
	 * 
	 * if (!Application.appUser.isInitialized())
	 *     return HomeController.unauthResponse();
	 * 
	 * or this:
	 * 
	 * if (!Application.appUser.getType().equals(AppUser.TYPE_TEACHING_ADMIN))
	 *     return HomeController.unauthResponse();
	 *     
	 * Note (Gabrielius): This kind of redirection could be achieved more neatly
	 *   using interceptor classes, but I don't know how to use them yet.
	 **/
	public static String unauthResponse() {
		if (Application.appUser.isInitialized())
			return "redirect:/";
		else
			return "redirect:/signin";
	}
	
	@ModelAttribute("appUser")
    public AppUser getAppUser() {
        return Application.appUser;
    }
}
