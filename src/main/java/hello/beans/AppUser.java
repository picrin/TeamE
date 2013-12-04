package hello.beans;

import org.springframework.context.annotation.Scope;
import org.springframework.context.annotation.ScopedProxyMode;
import org.springframework.stereotype.Component;

@Component
@Scope(value="session", proxyMode=ScopedProxyMode.TARGET_CLASS)
public class AppUser {
	
	//These values are used in templates
	public static final String TYPE_STUDENT = "student";
	public static final String TYPE_TEACHING_ADMIN = "teach_admin";
	
	private String type = "";
	private String username = "";
	
	public String getType() {
		return type;
	}
	public void setType(String type) {
		this.type = type;
	}
	public String getUsername() {
		return username;
	}
	public void setUsername(String username) {
		this.username = username;
	}
	
	public boolean isInitialized() {
		return (type != null) && type.length() > 0;
	}
	
}
