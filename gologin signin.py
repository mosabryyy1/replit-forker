# pip install selenium-stealth

#system libraries
from selenium import webdriver
from selenium_stealth import stealth
import random
from random import randint
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException


print (' ')
print ("Starting ...")
print (' ')


#######################################################################
#options = webdriver.ChromeOptions()
#options.add_argument("user-data-dir=C:\\Users\\Home Pc\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2\\Default")
#options.add_argument("--incognito")
#options.add_argument('--no-sandbox')
#options.add_argument("--start-maximized")
#options.add_argument('--disable-dev-shm-usage')
#options.add_experimental_option("excludeSwitches", ["enable-automation"])
#options.add_experimental_option('useAutomationExtension', False)
#options.add_argument("--headless")
#browser = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

###############################|  DETAILS  |###############################

emailadd = "eadptqie@knowledgemd.com"
password = "eadptqie@knowledgemd.com"
time.sleep(5)

#################################| ACCOUNT SIN |##############################


browser.get("https://app.gologin.com/#/sign_in")
time.sleep(5)
browser.implicitly_wait(30)
print("WebSite --> Fully Lodded")

email_input = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/form/input[1]").send_keys(emailadd)
time.sleep(3)
browser.implicitly_wait(30)

pass_input = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/form/input[2]").send_keys(password)
time.sleep(4)
browser.implicitly_wait(30)

signin_btn = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/form/button").click()
time.sleep(30)
browser.implicitly_wait(30)


browser.get("https://app.gologin.com/#/profileList")
time.sleep(5)

browser.implicitly_wait(30)
run_btn = browser.find_element_by_xpath("/html/body/div[1]/div/section/main/div/div[3]/div/div/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[6]/div/button").click()


time.sleep(5)
browser.implicitly_wait(30)
#view_btn = browser.find_element_by_xpath("/html/body/div[1]/div/section/main/div/div[3]/div/div/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[6]/div/button[1]/a").click()
browser.execute_script('document.querySelector("#root > div > section > main > div > div.infinite-scroll-component__outerdiv > div > div > div.ant-table-wrapper.css-1iyl7mu > div > div > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(6) > div > button.ant-btn.css-1xdc6ze.ant-btn-sm > a").click()')


print("RUNNING...")


for i in range(99999999):
	time.sleep(5000)
	#browser.switch_to.window(browser.window_handles[0])
