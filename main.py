from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
from time import sleep
from threading import Thread


BASE_URL="https://mobin.uk.ac.ir/"
USERNAME="test"
PASSWORD="testPass"

def threaded_function2():
    sleep(10)
    pyautogui.press('tab')
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('enter')
thread2 = Thread(target = threaded_function2)
thread2.start()

driver = webdriver.Chrome()

driver.get(BASE_URL)
driver.maximize_window()
usernameFiled = driver.find_element_by_name("UserName")
usernameFiled.send_keys(USERNAME)
passwordFiled = driver.find_element_by_name("Password")
passwordFiled.send_keys(PASSWORD)
passwordFiled.send_keys(Keys.RETURN)

mobinWindowId = driver.current_window_handle

enterClass = driver.find_element_by_link_text('ورود')
enterClass.click()
print(driver.title)

chwd = driver.window_handles
for w in chwd:
    if w != mobinWindowId:
        driver.switch_to.window(w)


driver.execute_script("openInBrowser()")

# sleep(10)
#
# pyautogui.press('tab')
# pyautogui.press('enter')
#
# sleep(20)
#
# pyautogui.press('tab')
# pyautogui.press('tab')
# pyautogui.press('enter')
# # openInAppBtn = driver.find_element_by_class_name("open-in-app-button").click()



