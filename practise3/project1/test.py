with open("/Applications/Python 3.10/code/practise3/project1/account.txt", 'r+') as f:
    acc=f.readline()
    pw=f.readline()
print(acc.strip())
with open("/Applications/Python 3.10/code/practise3/project1/content.txt","r+") as f:
    file=f.read()
    content=" ".join(file.split())
print(file)
# import webdriver
from selenium import webdriver

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

# import KEYS
from selenium.webdriver.common.keys import Keys

# create webdriver object
driver = webdriver.Chrome()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# create action chain object
action = ActionChains(driver)

# perform the operation
action.key_down(Keys.CONTROL).send_keys('F').key_up(Keys.CONTROL).perform()

