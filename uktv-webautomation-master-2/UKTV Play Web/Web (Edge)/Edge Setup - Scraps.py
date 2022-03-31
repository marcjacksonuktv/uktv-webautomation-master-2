desired_cap = {}
driver = webdriver.Edge(executable_path='/Users/james.stott/PycharmProjects/venv/Selenium/Remote/msedgedriver', capabilities=desired_cap)
testurl = 'https://uktv:wemakegreattv@uktvplay.uatuktv.co.uk/'


from webdriver_manager.microsoft import EdgeChromiumDriverManager
desired_cap = {}
driver = webdriver.Edge(EdgeChromiumDriverManager().install())