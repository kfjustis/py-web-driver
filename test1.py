from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=1, size=(0, 0))
display.start()

browser = webdriver.Chrome()
browser.get('http://www.google.com')
print (str(browser.title))
browser.quit()

display.stop()
