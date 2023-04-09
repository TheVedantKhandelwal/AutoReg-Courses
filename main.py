'''from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
options = Options()
options.add_argument("start-maximized")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

browser.get('https://firstyear.bmsce.ttcindia.co')
wait = WebDriverWait(browser,10)
user=""
passw=""


browser.find_element_by_id("email").send_keys(user)
browser.find_element_by_id("password").send_keys(passw)
browser.find_element_by_class("w-full bg-blue-600 p-2 rounded-md text-white hover:bg-blue-500 flex justify-center").click()
browser.find_element_by_class("font-semibold cursor-pointer hover:text-blue-700 false").click()


browser.find_element(By.ID, "email").send_keys(user)
browser.find_element(By.ID,"password").send_keys(passw)
browser.find_element(By.CLASS_NAME,"w-full bg-blue-600 p-2 rounded-md text-white hover:bg-blue-500 flex justify-center") 
browser.find_element(By.CLASS_NAME,"font-semibold cursor-pointer hover:text-blue-700 false")

'''



'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("start-maximized")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

browser.get('https://firstyear.bmsce.ttcindia.co')
wait = WebDriverWait(browser, 10)
user = ""
passw = ""

email_elem = wait.until(EC.presence_of_element_located((By.ID, "email")))
email_elem.send_keys(user)

password_elem = wait.until(EC.presence_of_element_located((By.ID, "password")))
password_elem.send_keys(passw)

submit_elem = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign in')]")))
submit_elem.click()

profile_elem = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'font-semibold')]")))
profile_elem.click()

'''
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user=str(input("Your_Email_Here"))
passw=str(input("Your_Pass_Here"))

options = Options()
options.add_argument("start-maximized")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

browser.get('https://firstyear.bmsce.ttcindia.co')
wait = WebDriverWait(browser,10)

user=str(input("Your_Email_Here"))
passw=str(input("Your_Pass_Here"))

# Find the email input element and enter the user email
email_elem = wait.until(EC.presence_of_element_located((By.ID, "email")))
email_elem.send_keys(user)

# Find the password input element and enter the user password
password_elem = wait.until(EC.presence_of_element_located((By.ID, "password")))
password_elem.send_keys(passw)

# Find the login button and click on it
login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".w-full.bg-blue-600.p-2.rounded-md.text-white.hover:bg-blue-500.flex.justify-center")))
login_btn.click()

# Find the profile button and click on it
profile_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".font-semibold.cursor-pointer.hover:text-blue-700.false")))
profile_btn.click()

'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user = str(input("Username : "))
passw= str(input("Password : "))

options = Options()
options.add_argument("start-maximized")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


browser.get('https://firstyear.bmsce.ttcindia.co')

wait = WebDriverWait(browser, 10)


email_elem = wait.until(EC.visibility_of_element_located((By.ID, "email")))
email_elem.send_keys(user)

pass_elem = wait.until(EC.visibility_of_element_located((By.ID, "password")))
pass_elem.send_keys(passw)

login_elem = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]")))
login_elem.click()

reg_elem = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/nav/div/div[2]/ul/a[3]")))
reg_elem.click()

ASC1 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/tr[1]/td[5]/button")))
ASC1.click()

ASC2 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/tr[2]/td[5]/button")))
ASC.click()

ESC = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/tr[3]/td[5]/button")))
ESC.click()

ESC1choice = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/div/div/div[3]/table/tbody/tr[2]/td[5]/button")))
ESC1choice.click()
ESC1conf = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/div/div/div[4]/button")))
ESC1conf.click()
ESC1 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/tr[4]/td[5]/button")))
ESC1.click

ETCchoice = wait.until(EC.element_to_be_clickable((XPATH, "/html/body/div/div/div[2]/table/tbody/div/div/div[3]/table/tbody/tr[2]/td[5]/button")))
ETCchoice.click()
ETCconf = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/div/div/div[5]/button")))
ETCconf.click()
ETC = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/tr[5]/td[5]/button")))

AEC1 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/tr[6]/td[5]/button")))
AEC1.click()

HSMC = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/tr[7]/td[5]/button")))
HSMC.click()

SDC = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/tr[8]/td[5]/button")))
SDC.click()

input()
