from selenium import webdriver
from selenium.webdriver.common.keys import Keys



BASE_URL="https://mobin.uk.ac.ir/"
USERNAME="test"
PASSWORD="testPass"


driver = webdriver.Chrome()

driver.get(BASE_URL)

usernameFiled = driver.find_element_by_name("UserName")
usernameFiled.send_keys(USERNAME)
passwordFiled = driver.find_element_by_name("Password")
passwordFiled.send_keys(PASSWORD)
passwordFiled.send_keys(Keys.RETURN)




