##  import packages ##
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time
from datetime import datetime, timedelta
from configparser import ConfigParser

##  Initialize Config Parser and read values    ##
config_obj = ConfigParser()
config_obj.read("config.ini", encoding='utf-8')

misc = config_obj["miscellaneous"]
personal = config_obj["personal_info"]
contact = config_obj["contact_details"]
address = config_obj["address"]

##  Get next day value in format Weekday DD Month, Year (example: Sunday 30 January, 2022)  ##
tomorrow = datetime.today() + timedelta(1)
tomorrow_date = tomorrow.strftime("%A %B %#d, %Y")

##  initialize chromedriver and open covid test booking website ##
options = webdriver.ChromeOptions()
options.add_argument('--headless')  #runs in background
driver = webdriver.Chrome(executable_path = misc["chrome_driver_path"], options=options)
driver.get(misc["covid_url"])

##  Fill values in form ##
##  Select test day ##
sel = Select(driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div/form/div[5]/div[1]/div/div[1]/select"))
sel.select_by_visible_text(tomorrow_date)

# ##  Select Time ##
# ##  The time field is of type listbox and not a standard dropdown. Hence, the field has to first be clicked in order to reveal possible options, after which the value can be selected.  ##
time.sleep(3)   #add waiting time in order to navigate to list time field 
WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/main/div/div/form/div[5]/div[2]/div/div[1]/button/div[2]/span"))).click()
time.sleep(3)   #add waiting time to open list
WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/main/div/div/form/div[5]/div[2]/div/div[1]/div/ul/li[27]"))).click()

# ##  Select Gender   ##
driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div/form/div[6]/div[1]/div[1]/div/label[2]/input").click()

# ##  Fill text values    ##
driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div/form/div[6]/div[2]/div[1]/div/input").send_keys(personal["first_name"])
driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div/form/div[6]/div[2]/div[2]/div/input").send_keys(personal["last_name"])
driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div/form/div[6]/div[3]/div/div[1]/input[1]").send_keys(personal["birth_day"])
driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div/form/div[6]/div[3]/div/div[1]/input[2]").send_keys(personal["birth_month"])
driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div/form/div[6]/div[3]/div/div[1]/input[3]").send_keys(personal["birth_year"])
driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div/form/div[6]/div[4]/div/div/input").send_keys(contact["email_id"])
driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div/form/div[6]/div[5]/div[2]/div[1]/input").send_keys(contact["mobile_no"])
driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div/form/div[6]/div[7]/div/div/input").send_keys(address["street"])
driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div/form/div[6]/div[8]/div[1]/div/input").send_keys(address["post_code"])
driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div/form/div[6]/div[8]/div[2]/div/input").send_keys(address["city"])

# ##  Agree to Privacy and Consent    ##
driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div/form/div[9]/div/button").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div/form/div[10]/div/button").click()

##  Register for appointment    ##
# driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div/form/div[14]/div/button").click()

##  Keep browser open until appointment has been booked ## 
time.sleep(10)