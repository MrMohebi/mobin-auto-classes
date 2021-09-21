from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
from time import sleep
from threading import Thread


BASE_URL="https://mobin.uk.ac.ir/"
USERNAME="test"
PASSWORD="testPass"

# cancel certificate pop up
def threaded_function2():
    sleep(10)
    pyautogui.press('tab')
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('enter')
thread2 = Thread(target = threaded_function2)
thread2.start()

# open site
driver = webdriver.Chrome()
driver.get(BASE_URL)
driver.maximize_window()

# login
usernameFiled = driver.find_element_by_name("UserName")
usernameFiled.send_keys(USERNAME)
passwordFiled = driver.find_element_by_name("Password")
passwordFiled.send_keys(PASSWORD)
passwordFiled.send_keys(Keys.RETURN)

# go to open class
mobinWindowId = driver.current_window_handle
enterClass = driver.find_element_by_link_text('ورود')
enterClass.click()

#change default window to new tab(select open in web or app)
chwd = driver.window_handles
for w in chwd:
    if w != mobinWindowId:
        driver.switch_to.window(w)

# open class in web
driver.execute_script("openInBrowser()")

# # open class in app
# driver.execute_script("openInApplication()")
# sleep(5)
# pyautogui.press('tab')
# pyautogui.press('tab')
# pyautogui.press('enter')



