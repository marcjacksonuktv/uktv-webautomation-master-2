import sys
import time
from time import gmtime, strftime
import datetime
import conf as conf
import self as self
now = datetime.datetime.now()
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.opera import OperaDriverManager
driver = webdriver.Opera(executable_path=OperaDriverManager().install())
testurl = 'https://uktv:wemakegreattv@uktvplay.ppdevuktv.co.uk/'
driver.set_window_size(500, 1000)
a = ActionChains(driver)
driver.get(testurl)
driver.implicitly_wait(10)

# Cookie Notice
CookieYes = driver.find_element(By.ID,'cookie-agree')
CookieYes.click()

time.sleep(2)

# -- Scroll Page --
ScrollPage = driver.find_element(By.TAG_NAME,'body')
ScrollPage.send_keys(Keys.END)

# -- Footer --
logofooter = driver.find_element(By.XPATH,'//*[@id="app"]/footer/div/div[1]/a/img')

help = driver.find_element(By.ID,'footer-help')
print(help.get_attribute('href'))
TVregistration = driver.find_element(By.ID,'footer-TVreg')
print(TVregistration.get_attribute('href'))
ContactUs = driver.find_element(By.ID,'footer-contact')
print(ContactUs.get_attribute('href'))
ParentalGuidance = driver.find_element(By.ID,'footer-PIN')
print(ParentalGuidance.get_attribute('href'))
WaystoWatch = driver.find_element(By.ID,'footer-ways')
print(WaystoWatch.get_attribute('href'))

# -- General --

PrivacyPolicy = driver.find_element(By.ID,'footer-privacy')
print(PrivacyPolicy.get_attribute('href'))
TandC = driver.find_element(By.ID,'footer-terms')
print(TandC.get_attribute('href'))
Accessibility = driver.find_element(By.ID,'footer-accessibility')
print(Accessibility.get_attribute('href'))
CookieFooter = driver.find_element(By.ID,'footer-cookie')
print(CookieFooter.get_attribute('href'))
Corp = driver.find_element(By.ID,'footer-corporate')
print(Corp.get_attribute('href'))
Footerchannels = driver.find_element(By.ID,'footer-channels')
print(Footerchannels.get_attribute('href'))
Slavery = driver.find_element(By.ID,'footer-slavery')
print(Slavery.get_attribute('href'))

# -- Social Feeds Links --

Twitter = driver.find_element(By.ID,'footer-twitter')
print(Twitter.get_attribute('href'))
Facebook = driver.find_element(By.ID,'footer-facebook')
print(Facebook.get_attribute('href'))
Instagram = driver.find_element(By.ID,'footer-instagram')
print(Instagram.get_attribute('href'))