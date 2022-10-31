from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

driver=webdriver.Safari()
time.sleep(5)

# url='https://onedrive.live.com/about/vi-vn/signin/'
url="https://www.facebook.com"
# url='https://shopee.vn/Tranh-Vải-Hoạt-Hình-Treo-Tường-Trang-Tr%C3%AD-Phòng-Ngủ-i.80205807.11700246291?sp_atk=c3bbbaaa-dcc8-4911-9922-51abefb2ffd2&xptdk=c3bbbaaa-dcc8-4911-9922-51abefb2ffd2'
driver.get(url)
# driver.implicitly_wait(5)
# time.sleep(5)
# driver.execute_script('window.scrollTo(0, 2200)')
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,'#main > div > div:nth-child(3) > div.XmiBHs > div > div.page-product > div > div.bON-xL > div.page-product__content > div.page-product__content--left > div:nth-child(2) > div > div.product-rating-overview > div.product-rating-overview__filters > div:nth-child(2)').click()

# time.sleep(2)
# driver.find_element(By.NAME,'pass').send_keys(KEY_ENTER)
# time.sleep(2)
# driver.find_element(By.NAME,'login').click()

