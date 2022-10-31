from selenium import webdriver # import function for using website automatically, selenium is just framework
from selenium.webdriver.common.by import By # for finding elements
from selenium.webdriver.common.keys import Keys  # to send_keys Enter
from selenium.webdriver.chrome.service import Service # access chromedriver
from selenium.webdriver.chrome.options import Options  # for handle pop-up
# from webdriver_manager.chrome import ChromeDriverManager # find address
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #wait 
from selenium.webdriver.common.action_chains import ActionChains
import time
import random


# set auto turn off notification pop-up. Set directly at Chrome options which is not relate to website
chrome_options = Options()
# chrome_options.add_argument('window-size=700x560')
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path='/Applications/Python 3.10/code/practise3/project1/chromedriver',options=chrome_options)


# Access facebook by given link
driver.set_window_size(900,900)
driver.implicitly_wait(5)
for i in range(100):
    url="https://vt.tiktok.com/ZSR4Ff922/"
    driver.get(url)
    time.sleep(20)
