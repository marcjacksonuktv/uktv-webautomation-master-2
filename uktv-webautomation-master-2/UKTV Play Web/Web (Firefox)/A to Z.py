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
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
testurl = 'https://uktvplay.uktv.co.uk/'
driver.get(testurl)
a = ActionChains(driver)
driver.implicitly_wait(15)

# Cookie Notice
CookieYes = driver.find_element_by_id('cookie-agree').click()

# Header
uktvplaylogo = driver.find_element_by_id('nav-bar-home')
categories = driver.find_element_by_id('nav-bar-categories')
channels = driver.find_element_by_id('nav-bar-channels')
boxsets = driver.find_element_by_id('nav-bar-boxsets')
a2z = driver.find_element_by_id('nav-bar-az')
more = driver.find_element_by_id('nav-bar-more')
mylist = driver.find_element_by_id('nav-bar-mylist')
account = driver.find_element_by_id('nav-bar-account')
search = driver.find_element_by_id('nav-bar-search')

# Sign In
account.click()
email = driver.find_element_by_id('email').send_keys('firefoxuser@testaccount.com')
password = driver.find_element_by_id('password').send_keys('password123')
SignIn_button = driver.find_element_by_id('sign-in-btn').click()
time.sleep(3)

# A to Z
a2z = driver.find_element_by_id('nav-bar-az').click()
time.sleep(2)
# subcontent buttons awiting Id's added
a = driver.find_element_by_id('atoz-A').click()
b = driver.find_element_by_id('atoz-B').click()
c = driver.find_element_by_id('atoz-C').click()
d = driver.find_element_by_id('atoz-D').click()
e = driver.find_element_by_id('atoz-E').click()
f = driver.find_element_by_id('atoz-F').click()
g = driver.find_element_by_id('atoz-G').click()
h = driver.find_element_by_id('atoz-H').click()
i = driver.find_element_by_id('atoz-I').click()
j = driver.find_element_by_id('atoz-J').click()
k = driver.find_element_by_id('atoz-K').click()
l = driver.find_element_by_id('atoz-L').click()
m = driver.find_element_by_id('atoz-M').click()
n = driver.find_element_by_id('atoz-N').click()
o = driver.find_element_by_id('atoz-O')
p = driver.find_element_by_id('atoz-P').click()
q = driver.find_element_by_id('atoz-Q').click()
r = driver.find_element_by_id('atoz-R').click()
s = driver.find_element_by_id('atoz-S').click()
t = driver.find_element_by_id('atoz-T').click()
u = driver.find_element_by_id('atoz-U').click()
v = driver.find_element_by_id('atoz-V').click()
w = driver.find_element_by_id('atoz-W').click()
x = driver.find_element_by_id('atoz-X')
y = driver.find_element_by_id('atoz-Y').click()
z = driver.find_element_by_id('atoz-Z').click()
num = driver.find_element_by_id('atoz-0-9').click()

print('A to Z passed')
