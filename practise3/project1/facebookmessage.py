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
url="https://www.facebook.com"
driver.get(url)

# Login step
with open("/Applications/Python 3.10/code/practise3/project1/account.txt", 'r+') as f:
    acc=f.readline()
    pw=f.readline()
driver.implicitly_wait(5)
acc_element=driver.find_element(By.NAME,'email')
acc_element.send_keys(acc.strip())
time.sleep(random.randrange(1,5))
pw_element=driver.find_element(By.NAME,"pass")
pw_element.send_keys(pw + Keys.ENTER)

# Access file of memmbers' link facebook 
with open("/Applications/Python 3.10/code/practise3/project1/link.txt","r") as f:
    lst=f.readlines()
link_lst=[]
for i in lst:
    if i!="\n":
        link_lst.append(i.strip())
    else: break

#prepare for message
with open("/Applications/Python 3.10/code/practise3/project1/content.txt","r+") as f:
    file=f.readlines()
    content="".join(file)


# Send message
wait = WebDriverWait(driver, 10)
locator= (By.XPATH,'/html/body/div[1]/div/div[1]/div/div[2]/div[1]/a')
wait.until(EC.visibility_of_element_located(locator))

with open("/Applications/Python 3.10/code/practise3/project1/content.txt","r+") as f:
    for i in link_lst:
    # Access profile link
        driver.get(i)
    # Open chatbox
        wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div/div[1]/div[2]/span/span")))
        Nhantin_icon_element=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div/div[1]/div[2]/span/span")
        Nhantin_icon_element.click()
    # Send given massage
        time.sleep(20)
        act=ActionChains(driver)
        chatbar=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p')
        typedchatbar=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div/p')

        for line in f:
            # point to this element
            act.move_to_element(chatbar).send_keys(line.strip()).perform()
            act.reset_actions()
            act.move_to_element(typedchatbar).key_down(Keys.SHIFT).send_keys(Keys.ENTER).perform()
            act.reset_actions()
            chatbar=typedchatbar
        f.seek(0)
        # send click
        typedchatbar.send_keys(Keys.ENTER)

    # Close chatbox
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/span[4]/div").click()



# time.sleep(5)
driver.close()

