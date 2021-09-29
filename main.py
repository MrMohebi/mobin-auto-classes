from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import pyautogui
from time import sleep
import re

BASE_URL="https://mobin.uk.ac.ir/"
USERNAME="testUsername"
PASSWORD="testPassword"
PROFILE_PATH = webdriver.FirefoxProfile("C:\\Users\\mrm\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\5icm3xnb.for-selenium")

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
driver = webdriver.Firefox(firefox_profile=PROFILE_PATH)
driver.quit()


def stopRecording(msg=None)->bool:
    global isRecording, driver
    try:
        pyautogui.press('f8')
        isRecording = False
        driver.quit()
        print("stop recording!")
        if msg:
            print(msg)
        return True
    except:
        return False


def enterRecordClass(now:datetime)->bool:
    global isRecording, driver
    try:
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
        driver = webdriver.Firefox(firefox_profile=PROFILE_PATH)
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

        sleep(20)

        # change default window to new tab(select open in web or app)
        chwd = driver.window_handles
        for w in chwd:
            if w != mobinWindowId:
                driver.switch_to.window(w)

        sleep(20)

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
        return True
    except Exception as e:
        print(now.strftime("%b %d %I:%M:%S ") + "OpeningClass And Record: " + str(e))
        driver.quit()
    return False


def isStudentsPresent(studentNum, actionFunc = None)->bool:
    global driver
    try:
        participantsSpan = driver.find_elements_by_class_name("customAttendeeGroupText--2rjYZtoo93MfQO6S0VwQbr")
        participantsNumber = int(list(filter(None, re.split('\)|\(|\s', participantsSpan[2].text)))[1])
        if participantsNumber < studentNum:
            if actionFunc:
                actionFunc()
            return False
    except:
        pass
    return True


def isClassStarted(actionFunc = None)->bool:
    global driver
    try:
        waitingMessage = driver.find_element_by_id("waitingScreenMessage")
        if waitingMessage.text.len() > 1:
            if actionFunc:
                actionFunc()
            return False
    except:
        pass
    return True



if __name__ == "__main__":
    # check each 5 min
    while True:
        now = datetime.datetime.now()
        todayClasses = classTime[now.strftime("%A")]
        try:
            if (now.hour in todayClasses) and (46 > now.minute > 30) and (isRecording == False):
                enterRecordClass(now)
            elif (now.hour-2 in todayClasses) and (24 < now.minute < 30) and (isRecording == True):
                stopRecording()

            #check class
            else:
                if isRecording:
                    driver.switch_to.frame(driver.find_element_by_id("html-meeting-frame"))
                    # check class after 20 minutes
                    if (now.hour in todayClasses) and (59 > now.minute > 50):
                        # if there is less than 5 student in class, close class
                        isStudentsPresent(5, lambda: stopRecording("there is no student in class"))

                        #if class didn't start, close and stop recording
                        isClassStarted(lambda: stopRecording("class didn't start"))

        except Exception as e:
            print(now.strftime("%b %d %I:%M:%S ") + str(e))

        sleep(300)

