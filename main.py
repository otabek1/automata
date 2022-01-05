from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from names import names

browser = webdriver.Chrome("./chromedriver")
browser.get("https://usflearn.instructure.com/conversations#filter=type=inbox")

EMAILFIELD = (By.ID, "i0116")
PASSWORDFIELD = (By.ID, "i0118")
NEXTBUTTON = (By.ID, "idSIButton9")
OTPFIELD = (By.ID, "idTxtBx_SAOTCC_OTC")
VERIFYBUTTON = (By.ID, "idSubmit_SAOTCC_Continue")
COMPOSEBUTTON = (By.ID, "compose-btn")

COURSE1 = (
    By.XPATH, "/html/body/div[4]/div[3]/form/div[1]/div/div[1]/div[2]/div/button")
COURSE2 = (
    By.XPATH, "/html/body/div[4]/div[3]/form/div[1]/div/div[1]/div[2]/div/div/ul/li[2]/a")

COURSE3 = (
    By.XPATH, "/html/body/div[4]/div[3]/form/div[1]/div/div[1]/div[2]/div/div/ul/li[2]/div[2]/ul/li[2]/a/abbr")


# print(input.get_attribute("placeholder"))
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
    EMAILFIELD)).send_keys("Your email")

WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable(NEXTBUTTON)).click()

WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
    PASSWORDFIELD)).send_keys("Your password")

WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable(NEXTBUTTON)).click()
browser.execute_script(
    "var a = prompt('Enter Verification Code', '');document.body.setAttribute('data-id', a)")
time.sleep(9) 
otp = browser.find_element(By.TAG_NAME, 'body').get_attribute('data-id')
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
    OTPFIELD)).send_keys(otp)

WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable(VERIFYBUTTON)).click()
WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable(NEXTBUTTON)).click()

WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable(COMPOSEBUTTON)).click()

WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable(COURSE1)).click()
WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable(COURSE2)).click()
COURSE3 = (
    By.XPATH, "/html/body/div[4]/div[3]/form/div[1]/div/div[1]/div[2]/div/div/ul/li[2]/div[2]/ul/li[2]/a/abbr")

WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable(COURSE3)).click()
RECEIPIENTS = (
    By.XPATH, "/html/body/div[4]/div[3]/form/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/input")
    
for name in names:
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(RECEIPIENTS)).send_keys(name)
    time.sleep(3)
    webdriver.ActionChains(browser).key_down(Keys.ENTER).perform()


