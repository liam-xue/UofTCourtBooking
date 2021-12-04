import importlib
try:
    importlib.import_module('selenium')
except ImportError:
    import pip
    pip.main(['install', 'selenium'])

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os, sys
import datetime
import ReadFile

def main():
    dic = ReadFile.readFile('BookingInfo.txt')
    pagelink = dic['Webpage']
    utorid = dic['UTORid']
    password = dic['Password']
    AutoReload = dic['AutoReload']
    dic = ReadFile.readFile('ConfirmBookingTime.txt')
    target_date = dic['BookingDate']
    target_time = dic['BookingTime']
    StartTime = dic['StartTime']
    refresh_time = datetime.datetime(StartTime[0],StartTime[1],StartTime[2],StartTime[3],StartTime[4]) - datetime.timedelta(days=2)

    cur_time = datetime.datetime.now()  # make sure it is at most 5 minutes early
    diff = refresh_time - cur_time
    if diff > datetime.timedelta(minutes=5):
        time.sleep(diff.seconds)

    driver.get(pagelink)    # open webpage
    action = ActionChains(driver)   # make page clickable
    wait = WebDriverWait(driver, 5) # setup wait timer

    return

    if not os.path.exists("ErrorLog.txt"):  # prepare the error log
        open("ErrorLog.txt","x")


    try:    # click login button
        wait.until(EC.presence_of_element_located((By.ID, 'loginLink'))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[@title='UTORid login for faculty, staff and students']"))).click()
    except:
        outputError('UNABLE_TO_FIND_LOGIN_BUTTON')

    try:    # type login credential and attempt login
        wait.until(EC.presence_of_element_located((By.ID, 'username'))).send_keys(utorid)
        wait.until(EC.presence_of_element_located((By.ID, 'password'))).send_keys(password)
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[@name='_eventId_proceed']"))).click()
    except:
        outputError('LOGIN_BUTTON_ERROR')
    try:    # if the password incorrect error is seen, show this error msg
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH, "//p[@class='form-element form-error']")))
        outputError('LOGIN_CREDENTIAL_ERROR')
    except:
        pass

    cur_time = datetime.datetime.now()
    while cur_time - refresh_time < datetime.timedelta(0):
        cur_time = datetime.datetime.now()
    driver.refresh()

    try:    # attempt to obtain the card with specified time
        card = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-instance-dates='"+target_date+"'and @data-instance-times='"+target_time+"']")))
    except:
        try:    # try again
            driver.refresh()
            card = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-instance-dates='"+target_date+"'and @data-instance-times='"+target_time+"']")))
        except:
            outputError('DATE_TIME_ERROR')

    try:    # click the register button
        card.find_element_by_xpath(".//button").click()
    except:
        outputError('EVENT_NOT_AVAILABLE')

    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnAccept']"))).click()
        #wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='checkoutButton']"))).ckick()  #will acctually checkout!
    except:
        outputError('UNABLE_TO_FINISH_TRANSACTION')

    # finished!
    #driver.quit()

    if AutoReload:
        ReadFile.reloadFile('ConfirmBooking.txt',dic)


def outputError(error):
    f = open("ErrorLog.txt",'a')
    f.write(str(datetime.datetime.now())+'  '+error+'\n')
    f.close()
    #driver.quit()
    #sys.exit()

if __name__ == "__main__":
    driver = webdriver.Chrome('chromedriver.exe')
    main()
    sys.exit()
