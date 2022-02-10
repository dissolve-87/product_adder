# 1
from selenium import webdriver
from os import getcwd, environ,path
from dotenv import load_dotenv

class Login:
    # login site
    def __init__(self):
        ass_path = path.dirname(path.dirname(__file__))
        load_dotenv(f'{ass_path}/asseset/.env')
        SITE = environ.get("SITE")
        MAIL = environ.get("MAIL")
        PASS = environ.get("PASS")
        driver_bin = f'{ass_path}/asseset/geckodriver'
        self.driver = webdriver.Firefox(executable_path=driver_bin)
        self.driver.get(SITE)
        self.driver.find_element_by_id("input-email").send_keys(MAIL)
        self.driver.find_element_by_id("input-password").send_keys(PASS)
        self.driver.find_element_by_css_selector('button.btn.btn-primary').click()
