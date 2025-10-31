# tests/test_login_logout.py

from pages.login_page import LoginPage
import config


def test_login_valid_credentials(page):
    login = LoginPage(page)
    login.navigate()
    login.login(config.USERNAME, config.PASSWORD)
    message = login.get_success_message()
    assert "Logged In Successfully" in message
    print("✅ Valid login successful")


def test_login_invalid_username(page):
    login = LoginPage(page)
    login.navigate()
    login.login("wronguser", config.PASSWORD)
    message = login.get_error_message()
    assert "Your username is invalid!" in message
    print("✅ Invalid username handled correctly")


def test_login_invalid_password(page):
    login = LoginPage(page)
    login.navigate()
    login.login(config.USERNAME, "wrongpassword")
    message = login.get_error_message()
    assert "Your password is invalid!" in message
    print("✅ Invalid password handled correctly")


def test_login_blank_fields(page):
    login = LoginPage(page)
    login.navigate()
    login.login("", "")
    message = login.get_error_message()
    assert "Your username is invalid!" in message  # site shows same message
    print("✅ Blank fields validation displayed")


def test_logout_functionality(page):
    login = LoginPage(page)
    login.navigate()
    login.login(config.USERNAME, config.PASSWORD)
    
    # Click Logout
    login.logout()
    
    # Assert user is back on login page
    page.wait_for_selector("h2")
    header_text = page.text_content("h2")
    assert "Test login" in header_text
    print("✅ Logout successful and redirected to Login Page")
