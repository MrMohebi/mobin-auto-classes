from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import pyautogui
from time import sleep


BASE_URL="https://mobin.uk.ac.ir/"
USERNAME="testUsername"
PASSWORD="testPassword"

classTime = {
    "Saturday":[9,13, 15],
    "Sunday":[9, 11],
    "Monday":[11, 13, 15],
    "Tuesday":[11],
    "Wednesday":[9, 11, 13],
    "Thursday":[],
    "Friday":[]
}

isRecording = False

# selenium web driver holder
driver = webdriver.Chrome("chromedriver")

# check each 5 min
while True:
    now = datetime.datetime.now()
    todayClasses = classTime[now.strftime("%A")]
    if (now.hour in todayClasses) and (36 < now.minute < 24) and (isRecording == False):
        print("class has been started on " + str(now.hour) + ":30")
        # cancel certificate pop up
        # def threaded_function2():
        #     sleep(10)
        #     pyautogui.press('tab')
        #     pyautogui.press('right')
        #     pyautogui.press('right')
        #     pyautogui.press('enter')
        # thread2 = Thread(target = threaded_function2)
        # thread2.start()

        # open site
        driver = webdriver.Chrome("chromedriver")
        driver.get(BASE_URL)
        driver.maximize_window()

        sleep(10)

        # login
        usernameFiled = driver.find_element_by_name("UserName")
        usernameFiled.send_keys(USERNAME)
        passwordFiled = driver.find_element_by_name("Password")
        passwordFiled.send_keys(PASSWORD)
        passwordFiled.send_keys(Keys.RETURN)

        sleep(10)

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

        # start recording
        pyautogui.press('f8')
        isRecording = True
        print("start recording")
    elif (now.hour-2 in todayClasses) and (38 < now.minute < 55) and (isRecording == True):
        pyautogui.press('f8')
        isRecording = False
        driver.quit()
        print("stop recording!")

    sleep(300)


