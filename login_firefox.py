import sys
import time
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver import ActionChains

display = Display(visible=0, size=(0, 0))
display.start()

browser = webdriver.Firefox()
browser.get("http://wikimapia.org/api/?action=create_key")

# need to check if logged in or not...
global need_login
need_login = False
login_link = None
print("===DEBUG===")
try:
    login_link = browser.find_element_by_link_text("login or register")
    if str(login_link.text) == "login or register":
        need_login = True
        print("First login value: " + str(need_login))
    else:
        need_login = False
        print("First login value: " + str(need_login))
except:
    print("(1) Could not find requested element.")

# try to login if we need to
print("Outside login value: " + str(need_login))
if need_login:
    # navigate to login page
    print("Trying to login...")
    print("Current page: " + browser.title)
    actions = ActionChains(browser)
    actions.click(login_link)
    actions.perform()

    # load the new page
    i = 5
    while i > 0:
        print("Waiting for %s second(s)..." % i)
        time.sleep(1) # bad, don't keep this
        i = i - 1

    # find username/password box and login button from modal, then fill fields and submit
    try:
        #print("Current page: " + browser.title)
        browser.switch_to.frame(browser.find_element_by_id("wm-iframe-69"))
        username_field = browser.find_element_by_name("username")
        #print("\tFound username box -> " + str(username_field))
        password_field = browser.find_element_by_class_name("login-password")
        #print("\tFound password box -> " + str(username_field))
        login_button = browser.find_element_by_css_selector("input.login-submit")
        #print("Found login button -> " + str(username_field))
    except:
        print("(2) Could not find requested element.")

    uusername_field.send_keys("u_name_here")
    password_field.send_keys("p_word_here")

    actions = ActionChains(browser)
    actions.click(login_button)
    actions.perform()

    print("Returning to default context (main browser window)...")
    browser.switch_to.default_content()
    print("Login successful.")


# quit and close
print("===END DEBUG===")
print()
print("Completed all tasks.")
print()
i = 5
while i > 0:
    print("Terminating in %s second(s)..." % i)
    time.sleep(1) # bad, don't keep this
    i = i - 1
print()

browser.quit()
display.stop()
