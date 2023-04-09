from time import *
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
def _options():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    #options.add_argument("--test-type")
    options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument('--disable-gpu') if os.name == 'nt' else None # Windows workaround
    options.add_argument("--verbose")
    return options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import maskpass
user = str(input("Username : "))
#passw= str(input("Password : "))
passw=maskpass.askpass(prompt="Password : ",mask="*")

#htmlelement= browser.find_element_by_tag_name('html')
ChoiceESC = input("Choose your course for ESC-1 :\n1. Introduction to Civil Engg\n2. Introduction to Electrical Engg\n3. Introdution to Electronics Engg\n4. Introduction to Mechanical Engg\nYour Choice : ")
ChoiceETC = input("Choose your course for ETC :  \n1. Green Buildings\n2. Introductio to Sustainable Engineering\n3. Renewable Energy Sources\n4.Waste Management\nYour Choice : ")
options = Options()
options.add_argument("start-maximized")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
htmlelement = browser.find_element(By.TAG_NAME, 'html')
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
sleep(1)
ASC2 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/tr[2]/td[5]/button")))
ASC2.click()
sleep(1)
ESC = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/tr[3]/td[5]/button")))
ESC.click()
sleep(1)
#ESC1choice = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/div/div/div[3]/table/tbody/tr[2]/td[5]/button")))
#ESC1choice.click()
#ESC1conf = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/div/div/div[4]/button")))
#ESC1conf.click()
#ESC1 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/tr[4]/td[5]/button")))
#ESC1.click

sleep(1)
ESC1select = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/tr[4]/td[4]/div/button")))
ESC1select.click()
ESC1choice = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/div/div/div[3]/table/tbody/tr[{}]/td[5]/button".format(ChoiceESC))))
ESC1choice.click()
ESCconf = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/div/div/div[4]/button")))
ESCconf.click()
ESCreg = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/tr[4]/td[5]/button")))
ESCreg.click()
sleep(1)
#ETCchoice = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/div/div/div[3]/table/tbody/tr[2]/td[5]/button")))
#ETCchoice.click()
#ETCconf = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/div/div/div[5]/button")))
#ETCconf.click()

sleep(1)
ETCselect = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/tr[5]/td[4]/div/button")))
ETCselect.click()
ETCchoice = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/div/div/div[3]/table/tbody/tr[{}]/td[5]/button".format(ChoiceETC))))
ETCchoice.click()
ETCconf = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/div/div/div[5]/button")))
ETCconf.click()
ETCreg = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/tr[5]/td[5]/button")))
ETCreg.click()
htmlelement = browser.find_element(By.TAG_NAME, 'html')
htmlelement.send_keys(Keys.END)
sleep(1)
AEC1 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/tr[6]/td[5]/button")))
AEC1.click()
sleep(1)
HSMC = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/tr[7]/td[5]/button")))
HSMC.click()
sleep(1)
SDC = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/table/tbody/tr[8]/td[5]/button")))
SDC.click()

input()
