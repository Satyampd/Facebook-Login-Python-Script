from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time
 
driver = webdriver.Chrome("C:\\Users\\User\\Desktop\\chromedriver.exe")
driver.get('https://www.facebook.com/login.php?login_attempt=1&lwv=110')
print("Opened facebook...")
email = driver.find_element_by_xpath("//input[@id='email' or @name='email']")
email.send_keys('Your Email')
print("Email Id entered...")
password = driver.find_element_by_xpath("//input[@id='pass']")
password.send_keys('Password')
print("Password entered...")
button = driver.find_element_by_xpath("//button[@id='loginbutton']")
button.click()
print("FB opened")


statusbox = driver.find_element_by_xpath("//textarea[@name='xhpc_message']")
statusbox.send_keys("Bot is typing here");
print("Status trying")
postbutton = driver.find_element_by_xpath("//button[contains(.,'Post')]")
postbutton.click()
print("post done")


