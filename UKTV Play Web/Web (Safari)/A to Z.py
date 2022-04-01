import sys
import time
from time import gmtime, strftime
import datetime
import conf as conf
import self as self
now = datetime.datetime.now()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
options = Options()
from selenium import webdriver
driver = webdriver.Safari(executable_path = '/usr/bin/safaridriver')
testurl = 'https://uktvplay.uktv.co.uk/'
a = ActionChains(driver)
driver.get(testurl)
driver.implicitly_wait(15)

# Cookie Notice
CookieYes = driver.find_element(By.ID,'cookie-agree').click()

# Header
uktvplaylogo = driver.find_element(By.ID, 'nav-bar-home')
categories = driver.find_element(By.ID, 'nav-bar-categories')
channels = driver.find_element(By.ID, 'nav-bar-channels')
boxsets = driver.find_element(By.ID, 'nav-bar-boxsets')
a2z = driver.find_element(By.ID, 'nav-bar-az')
more = driver.find_element(By.ID, 'nav-bar-more')
mylist = driver.find_element(By.ID, 'nav-bar-mylist')
account = driver.find_element(By.ID, 'nav-bar-account')
search = driver.find_element(By.ID, 'nav-bar-search')
time.sleep(2)

# Sign In
account.click()
email = driver.find_element(By.ID, 'email').send_keys('safariuser@testaccount.com')
password = driver.find_element(By.ID, 'password').send_keys('Password123!!')
SignIn_button = driver.find_element(By.ID, 'sign-in-btn').click()
time.sleep(3)

# A to Z
a2z = driver.find_element(By.ID, 'nav-bar-az').click()
time.sleep(2)
# subcontent buttons awiting Id's added
a = driver.find_element(By.ID, 'atoz-A').click()
b = driver.find_element(By.ID, 'atoz-B').click()
c = driver.find_element(By.ID, 'atoz-C').click()
d = driver.find_element(By.ID, 'atoz-D').click()
e = driver.find_element(By.ID, 'atoz-E').click()
f = driver.find_element(By.ID, 'atoz-F').click()
g = driver.find_element(By.ID, 'atoz-G').click()
h = driver.find_element(By.ID, 'atoz-H').click()
i = driver.find_element(By.ID, 'atoz-I').click()
j = driver.find_element(By.ID, 'atoz-J').click()
k = driver.find_element(By.ID, 'atoz-K').click()
l = driver.find_element(By.ID, 'atoz-L').click()
m = driver.find_element(By.ID, 'atoz-M').click()
n = driver.find_element(By.ID, 'atoz-N').click()
o = driver.find_element(By.ID, 'atoz-O')
p = driver.find_element(By.ID, 'atoz-P').click()
q = driver.find_element(By.ID, 'atoz-Q').click()
r = driver.find_element(By.ID, 'atoz-R').click()
s = driver.find_element(By.ID, 'atoz-S').click()
t = driver.find_element(By.ID, 'atoz-T').click()
u = driver.find_element(By.ID, 'atoz-U').click()
v = driver.find_element(By.ID, 'atoz-V').click()
w = driver.find_element(By.ID, 'atoz-W').click()
x = driver.find_element(By.ID, 'atoz-X')
y = driver.find_element(By.ID, 'atoz-Y').click()
z = driver.find_element(By.ID, 'atoz-Z')
num = driver.find_element(By.ID, 'atoz-0-9').click()

print('A to Z passed')
