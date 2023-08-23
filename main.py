from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)

import time
from names import names
service = webdriver.chrome.service.Service(service_args=['--disable-build-check'], executable_path='/chromedriver')

browser = driver = webdriver.Chrome(service=service, options=chrome_options)
browser.get("https://usflearn.instructure.com/conversations#filter=type=inbox")



COURSE_NAME = 'Operating Systems'
EMAILFIELD = (By.ID, "i0116")
PASSWORDFIELD = (By.ID, "i0118")
NEXTBUTTON = (By.ID, "idSIButton9")
OTPFIELD = (By.ID, "idTxtBx_SAOTCC_OTC")
VERIFYBUTTON = (By.ID, "idSubmit_SAOTCC_Continue")
COMPOSEBUTTON = (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div[1]/div/div[2]/div/span[1]/div/div/span/span[4]/span/span[1]/span/span/button")

COURSE_INPUT = (By.XPATH, "/html/body/span[27]/span/span/div[2]/span/span[1]/span[1]/span/span[2]/span/label/span/span/span[2]/span/span/span/span/span[1]/input")

NAMES_INPUT = (
    By.XPATH, "/html/body/span[27]/span/span/div[2]/span/span[1]/span[3]/span/span[2]/div/div/span/span[1]/span/label/span/span/span[2]/span/span/span[2]/span/span/input")

    
# print(input.get_attribute("placeholder"))
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
    EMAILFIELD)).send_keys("YOUR email here ")

WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable(NEXTBUTTON)).click()

WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
    PASSWORDFIELD)).send_keys("YOUR password here")


WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable(NEXTBUTTON)).click()

time.sleep(5)
WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable(NEXTBUTTON)).click()
time.sleep(5)
print(browser.current_url)
WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable(COMPOSEBUTTON)).click()


WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable(COURSE_INPUT)).send_keys(COURSE_NAME)

webdriver.ActionChains(browser).key_down(Keys.ENTER).perform()




for name in names:
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(NAMES_INPUT)).send_keys(name)
    time.sleep(2)
    webdriver.ActionChains(browser).key_down(Keys.ENTER).perform()
