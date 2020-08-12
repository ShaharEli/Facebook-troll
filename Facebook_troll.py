from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from password import password1,user1 #password and username for facebook
#import random
import os
lk = os.path.join(os.getcwd(), "chromedriver",)
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(lk, options=chrome_options)

driver.get("https://www.facebook.com/")
user_name=driver.find_element_by_xpath('//*[@id="email"]')
user_name.send_keys(user1)
password=driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys(password1)
login=driver.find_element_by_xpath('//*[@id="u_0_b"]')
login.click()
sleep(6)
driver.get('https://www.facebook.com/tav.burkush')
sleep(3)
sendd=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div/div[2]/a')
sendd.click()
sleep(2)
messg=driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[1]/div/div/div[4]/div/div[1]/div/div/div/div/div/div[1]/div/div[2]/div[4]/div/div/div/span/div/div/div[2]/div/div/div/div')
counter=1
while True:
    lol="bulbul number: "+str(counter)+" 8============}"
    try:
        messg = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[1]/div/div/div[4]/div/div[1]/div/div/div/div/div/div[1]/div/div[2]/div[4]/div/div/div/span/div/div/div[2]/div/div/div/div')
        messg.send_keys(lol,Keys.ENTER)
    except:
        continue

    counter+=1
    print(counter-1)
    sleep(5)
