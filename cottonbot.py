from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import random as r 
import time

zipcodes = [35226, 35244, 35022, 35242, 35080, 35216, 35260]
fn = open('firstnames.txt', 'r', encoding= "utf-8")
ln = open('lastnames.txt', 'r', encoding="utf-8")

def genrandNum(x): 
    return r.randrange(0, x)
def spamthatPage():
    namef = fn.readlines()
    namefr = genrandNum(1000)
    namel = ln.readlines()
    namelr = genrandNum(1000)
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://greatamericanrivalry.com/garsxhof-sa-voting-2021-form/")
    time.sleep(5)
    firstname = driver.find_element_by_xpath('//*[@id="input_29_1_3"]')         
    firstname.send_keys(namef[namefr])
    time.sleep(5)
    lastname = driver.find_element_by_xpath('//*[@id="input_29_1_6"]')
    lastname.send_keys(namel[namelr])
    time.sleep(5)
    email = driver.find_element_by_xpath('//*[@id="input_29_2"]')
    remail = namef[namefr] +  namel[namelr] + str(r.randrange(0,2021)) + "@gmail.com"
    remail = str(remail)
    remail = remail.replace('\n', '')
    email.send_keys(remail)
    time.sleep(5)
    votingfor = Select(driver.find_element_by_xpath('//*[@id="input_29_17"]'))
    votingfor.select_by_value("Cotton Peters (Hoover High School)")
    time.sleep(5)
    yob = Select(driver.find_element_by_xpath('//*[@id="input_29_22"]'))
    yob.select_by_value("2003")
    time.sleep(5)
    state = Select(driver.find_element_by_xpath('//*[@id="input_29_21_4"]'))
    state.select_by_visible_text('Alabama')
    time.sleep(5)
    zipcode = driver.find_element_by_id('input_29_21_5')
    zipcode.send_keys(zipcodes[r.randrange(0,6)])
    time.sleep(5)
    submit = driver.find_element_by_xpath('//*[@id="gform_submit_button_29"]')
    submit.click()
    time.sleep(5)
    driver.quit()

while True: 
    spamthatPage()
    i = i + 1
    print("Voting for Cotton. This is vote:", i)