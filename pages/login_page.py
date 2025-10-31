# pages/login_page.py
import config

class LoginPage:
    def __init__(self, page):
        self.page = page
        # Locators
        self.username_input = "input#username"
        self.password_input = "input#password"
        self.login_button = "button#submit"
        self.error_message = "#error"
        self.success_message = "h1"
        
        

    def navigate(self):
        """Go to login page"""
        self.page.goto(f"{config.BASE_URL}")

    def login(self, username, password):
        """Fill login form and submit"""
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_error_message(self):
        """Return error message text"""
        return self.page.text_content(self.error_message)

    def get_success_message(self):
        """Return success message text"""
        return self.page.text_content(self.success_message)

    def logout(self):
        """Click logout button"""
        self.page.get_by_text("Log out").click()

